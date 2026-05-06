import json

with open("notas.txt", "w") as arquivo:
    arquivo.write("Este é um teste de gravação em TXT.")


clientes = {
    "1": {"nome": "Gabriel", "email": "gabriel@email.com"},
    "2": {"nome": "Daniel", "email": "daniel@email.com"}
}

try:

    with open("clientes.json", "w") as f:
        json.dump(clientes, f, indent=4)

    with open("clientes.json", "r") as f:
        dados_carregados = json.load(f)
        print("Dados carregados do JSON:", dados_carregados)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")

    import csv

def salvar_notas_csv(dados):
    with open("notas_alunos.csv", "w", newline="") as f:
        escritor = csv.writer(f)
        escritor.writerow(["Nome", "Nota"]) # Cabeçalho
        escritor.writerows(dados)


notas = [["Lucas", 8.5], ["Gabriel", 9.0], ["Daniel", 7.0]]
salvar_notas_csv(notas)
print("Arquivo CSV criado com sucesso!")
import json
import os

ARQUIVO_DB = "banco_clientes.json"

def carregar_dados():
    if not os.path.exists(ARQUIVO_DB):
        return {}
    with open(ARQUIVO_DB, "r") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DB, "w") as f:
        json.dump(dados, f, indent=4)

def registrar_cliente():
    db = carregar_dados()
    id_cliente = input("ID do cliente: ")
    nome = input("Nome: ")
    db[id_cliente] = {"nome": nome}
    salvar_dados(db)
    print("Cliente registrado!")

def consultar_cliente():
    db = carregar_dados()
    id_cliente = input("Digite o ID para consulta: ")
    cliente = db.get(id_cliente)
    if cliente:
        print(f"Cliente: {cliente['nome']}")
    else:
        print("Cliente não encontrado.")

    
import os

import shutil

def fazer_backup():
    origem = "banco_clientes.json"
    destino = "backup/banco_clientes_bkp.json"
    
  
    if not os.path.exists("backup"):
        os.makedirs("backup")
        
    try:
        shutil.copy2(origem, destino)
        print(f"Backup realizado com sucesso em: {destino}")
    except FileNotFoundError:
        print("Erro: Arquivo de origem não encontrado para backup.")