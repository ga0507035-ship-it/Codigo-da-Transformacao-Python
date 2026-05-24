import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = "usuarios_api.db"

def inicializar_banco():
    """Cria o banco e a tabela de usuários caso não existam (Atividade 3)."""
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conexao.commit()
    conexao.close()


# --- ROTA GET: SAUDAÇÃO (Atividade 1) ---
@app.route('/saudacao', methods=['GET'])
def obter_saudacao():
    """Retorna uma mensagem simples de boas-vindas em formato JSON."""
    return jsonify({
        "status": "sucesso",
        "mensagem": "Olá! Seja muito bem-vindo ao servidor Flask básico."
    }), 200


# --- ROTA POST: CADASTRAR COM SQLITE (Atividade 2 e 3) ---
@app.route('/cadastrar', methods=['POST'])
def cadastrar_usuario():
    """Recebe dados via JSON e insere na tabela SQLite."""
    # Captura o corpo da requisição JSON (Atividade 2)
    dados = request.get_json()
    
    # Validação simples para conferir se os campos foram enviados
    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({"erro": "Parâmetros 'nome' e 'email' são obrigatórios."}), 400
        
    nome_usuario = dados["nome"]
    email_usuario = dados["email"]
    
    # Conecta ao SQLite para salvar os dados (Atividade 3)
    try:
        conexao = sqlite3.connect(DATABASE)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Usuarios (nome, email) VALUES (?, ?)", (nome_usuario, email_usuario))
        conexao.commit()
        conexao.close()
        
        return jsonify({
            "status": "sucesso",
            "mensagem": f"Usuário '{nome_usuario}' registrado com sucesso!"
        }), 201
        
    except sqlite3.IntegrityError:
        return jsonify({"erro": f"O e-mail '{email_usuario}' já está cadastrado."}), 409
    except Exception as e:
        return jsonify({"erro": f"Houve um problema interno no servidor: {str(e)}"}), 500


# --- INICIALIZAÇÃO DO SERVIDOR ---
if __name__ == "__main__":
    # Garante a tabela criada antes do app subir
    inicializar_banco()
    
    # Executa o servidor local na porta 5000
    app.run(debug=True)
  import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
BLOG_DATABASE = "sistema_blog.db"

def preparar_ambiente_blog():
    """Configura o banco de dados relacional para o blog."""
    conexao = sqlite3.connect(BLOG_DATABASE)
    cursor = conexao.cursor()
    
    # 1. Tabela de Usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL
        )
    """)
    # 2. Tabela de Postagens (Relacionada ao Autor)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES Autores(id)
        )
    """)
    # 3. Tabela de Comentários (Relacionada ao Post)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post_id INTEGER NOT NULL,
            autor_nome TEXT NOT NULL,
            texto TEXT NOT NULL,
            FOREIGN KEY (post_id) REFERENCES Posts(id)
        )
    """)
    conexao.commit()
    conexao.close()


# --- MIDDLEWARE DE AUTENTICAÇÃO SIMULADA ---
def verificar_autorizacao():
    """Simulação de autenticação rápida pelo cabeçalho 'X-Autor-Id'."""
    autor_id = request.headers.get("X-Autor-Id")
    if not autor_id:
        return None
    return int(autor_id)


# --- ENDPOINTS DO BLOG ---

@app.route('/blog/registrar', methods=['POST'])
def registrar_autor():
    dados = request.get_json() or {}
    username = dados.get("username")
    senha = dados.get("senha")
    
    if not username or not senha:
        return jsonify({"erro": "Forneça username e senha."}), 400
        
    try:
        conn = sqlite3.connect(BLOG_DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Autores (username, senha) VALUES (?, ?)", (username, senha))
        conn.commit()
        autor_id = cursor.lastrowid
        conn.close()
        return jsonify({"mensagem": "Autor registrado!", "seu_id_para_login": autor_id}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este nome de usuário já existe."}), 409


@app.route('/blog/posts', methods=['POST'])
def criar_postagem():
    autor_logado = verificar_autorizacao()
    if not autor_logado:
        return jsonify({"erro": "Acesso negado. Passe seu ID no cabeçalho 'X-Autor-Id'."}), 401
        
    dados = request.get_json() or {}
    titulo = dados.get("titulo")
    conteudo = dados.get("conteudo")
    
    if not titulo or not conteudo:
        return jsonify({"erro": "O post precisa de um título e conteúdo."}), 400
        
    conn = sqlite3.connect(BLOG_DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)", (titulo, conteudo, autor_logado))
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
    
    return jsonify({"mensagem": "Post publicado!", "post_id": post_id}), 201


@app.route('/blog/posts', methods=['GET'])
def listar_postagens():
    conn = sqlite3.connect(BLOG_DATABASE)
    cursor = conn.cursor()
    # Traz o post e o nome do autor usando JOIN
    cursor.execute("""
        SELECT Posts.id, Posts.titulo, Posts.conteudo, Autores.username 
        FROM Posts JOIN Autores ON Posts.autor_id = Autores.id
    """)
    posts_db = cursor.fetchall()
    conn.close()
    
    resultado = []
    for p in posts_db:
        resultado.append({
            "id": p[0],
            "titulo": p[1],
            "conteudo": p[2],
            "autor": p[3]
        })
    return jsonify(resultado), 200


@app.route('/blog/posts/<int:post_id>/comentarios', methods=['POST'])
def adicionar_comentario(post_id):
    dados = request.get_json() or {}
    autor_nome = dados.get("autor_nome", "Anônimo")
    texto = dados.get("texto")
    
    if not texto:
        return jsonify({"erro": "O texto do comentário não pode estar vazio."}), 400
        
    conn = sqlite3.connect(BLOG_DATABASE)
    cursor = conn.cursor()
    
    # Verifica se o post alvo realmente existe
    cursor.execute("SELECT id FROM Posts WHERE id = ?", (post_id,))
    if not cursor.fetchone():
        conn.close()
        return jsonify({"erro": "O post informado não existe."}), 404
        
    cursor.execute("INSERT INTO Comentarios (post_id, autor_nome, texto) VALUES (?, ?, ?)", (post_id, autor_nome, texto))
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Comentário adicionado com sucesso!"}), 201


@app.route('/blog/posts/<int:post_id>/comentarios', methods=['GET'])
def listar_comentarios(post_id):
    conn = sqlite3.connect(BLOG_DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT autor_nome, texto FROM Comentarios WHERE post_id = ?", (post_id,))
    comentarios_db = cursor.fetchall()
    conn.close()
    
    resultado = [{"autor": c[0], "comentario": c[1]} for c in comentarios_db]
    return jsonify(resultado), 200


if __name__ == "__main__":
    preparar_ambiente_blog()
    app.run(port=5000, debug=True)
