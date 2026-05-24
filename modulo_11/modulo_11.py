import sqlite3

def inicializar_banco():
    """Conecta ao banco e cria a tabela Clientes se ela não existir (Atividade 1)."""
    conexao = sqlite3.connect("sistema_clientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)
    conexao.commit()
    return conexao


# --- OPERAÇÕES DO CRUD (Atividade 2) ---

def inserir_cliente(conexao, nome, email):
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print(f"✓ Cliente '{nome}' inserido com sucesso!")
    except sqlite3.IntegrityError:
        print(f"× Erro: O e-mail '{email}' já está cadastrado.")

def consultar_todos_clientes(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM Clientes")
    faturamento = cursor.fetchall()
    
    print("\n--- LISTA DE TODOS OS CLIENTES ---")
    for cliente in faturamento:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]}")
    print("-" * 35)

def atualizar_email_cliente(conexao, id_cliente, novo_email):
    cursor = conexao.cursor()
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"✓ E-mail do cliente ID {id_cliente} atualizado para '{novo_email}'.")
    else:
        print(f"× Cliente ID {id_cliente} não encontrado para atualização.")

def deletar_cliente(conexao, id_cliente):
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    if cursor.rowcount > 0:
        print(f"✓ Cliente ID {id_cliente} removido com sucesso.")
    else:
        print(f"× Cliente ID {id_cliente} não encontrado para exclusão.")


# --- CONSULTAS FILTRADAS (Atividade 3) ---

def buscar_clientes_por_inicial(conexao, letra):
    """Busca clientes cujo nome começa com uma letra específica usando LIKE."""
    cursor = conexao.cursor()
    # O comando "letra%" busca qualquer coisa que comece com aquela letra
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (f"{letra}%",))
    resultados = cursor.fetchall()
    
    print(f"\n--- CLIENTES QUE COMEÇAM COM A LETRA '{letra.upper()}' ---")
    if not resultados:
        print("Nenhum cliente encontrado.")
    for cliente in resultados:
        print(f"ID: {cliente[0]} | Nome: {cliente[1]} | E-mail: {cliente[2]}")
    print("-" * 45)


# --- EXECUÇÃO DOS TESTES ---
if __name__ == "__main__":
    # 1. Configura e cria o banco/tabela
    faturamento_db = inicializar_banco()
    
    # 2. Testando o CRUD: Inserir dados
    print("--- Inserindo Dados ---")
    inserir_cliente(faturamento_db, "Ana Costa", "ana.costa@email.com")
    inserir_cliente(faturamento_db, "Arthur Silva", "arthur@email.com")
    inserir_cliente(faturamento_db, "Carlos Souza", "carlos@email.com")
    
    # Consultar dados inseridos
    consultar_todos_clientes(faturamento_db)
    
    # Testando o CRUD: Atualizar dados (Atualizando o e-mail da Ana - ID 1)
    print("\n--- Atualizando Dados ---")
    atualizar_email_cliente(faturamento_db, 1, "ana.nova@email.com")
    
    # Testando a Atividade 3: Filtrar nomes que começam com "A"
    buscar_clientes_por_inicial(faturamento_db, "A")
    
    # Testando o CRUD: Deletar dados (Deletando o Carlos - ID 3)
    print("\n--- Deletando Dados ---")
    deletar_cliente(faturamento_db, 3)
    
    # Consulta final para ver como ficou o banco
    consultar_todos_clientes(faturamento_db)
    
    # Fecha a conexão com o banco de dados
    faturamento_db.close()
