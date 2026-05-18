print("--- Escrevendo no arquivo TXT ---")
with open("dados_simples.txt", "w", encoding="utf-8") as arquivo_txt:
    arquivo_txt.write("Linha 1: Introdução à manipulação de arquivos.\n")
    arquivo_txt.write("Linha 2: Este é um exemplo de armazenamento simples.\n")
    arquivo_txt.write("Linha 3: Fim do arquivo de texto.\n")
print("Dados gravados com sucesso!\n")


print("--- Lendo do arquivo TXT ---")
with open("dados_simples.txt", "r", encoding="utf-8") as arquivo_txt:
    conteudo = arquivo_txt.read()
    print(conteudo)
    

import json

clientes_dict = {
    "cliente_1": {
        "nome": "Ivan Paulino",
        "email": "Ivan.paulino@email.com",
        "ativo": True
    },
    "cliente_2": {
        "nome": " Daniel Freitas",
        "email": "Daniel.freitas@email.com",
        "ativo": False
    }
}


print("--- Salvando dados em JSON ---")
with open("clientes.json", "w", encoding="utf-8") as arquivo_json:
  
    json.dump(clientes_dict, arquivo_json, indent=4, ensure_ascii=False)
print("Dicionário de clientes salvo com sucesso!\n")


print("--- Carregando dados do JSON ---")
with open("clientes.json", "r", encoding="utf-8") as arquivo_json:
    dados_carregados = json.load(arquivo_json)
    
    for chave, info in dados_carregados.items():
        print(f"ID: {chave}")
        print(f"  Nome: {info['nome']}")
        print(f"  E-mail: {info['email']}")
        print(f"  Status: {'Ativo' if info['ativo'] else 'Inativo'}")


import csv


notas_alunos = [
    ["Nome", "Disciplina", "Nota"],
    ["Mariana", "Matemática", "18.5"],
    ["Pedro", "Física", "14.0"],
    ["Joana", "Química", "16.2"]
]


print("--- Gravando notas em CSV ---")

with open("notas_sistema.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv, delimiter=";")
    escritor_csv.writerows(notas_alunos)
print("Ficheiro CSV gerado com sucesso!\n")

print("--- Lendo notas do CSV ---")
with open("notas_sistema.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv, delimiter=";")
    
    for linha in leitor_csv:
        print(f"Aluno: {linha[0]:<10} | Disciplina: {linha[1]:<12} | Nota: {linha[2]}")

    import os
import shutil


pasta_origem = "documentos_importantes"
pasta_backup = "backup_sistema"

if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)
    # Cria um ficheiro fictício dentro da origem para teste
    with open(os.path.join(pasta_origem, "relatorio.txt"), "w") as f:
        f.write("Dados cruciais de backup.")
    print(f"Pasta '{pasta_origem}' criada para testes.")

if not os.path.exists(pasta_backup):
    os.makedirs(pasta_backup)

print("\n--- Iniciando Backup Automático ---")
try:
    ficheiros = os.listdir(pasta_origem)
    
    if not ficheiros:
        print("A pasta de origem está vazia. Nenhum arquivo para copiar.")
    else:
        for item in ficheiros:
            caminho_completo_origem = os.path.join(pasta_origem, item)
            caminho_completo_destino = os.path.join(pasta_backup, item)
            
            if os.path.isfile(caminho_completo_origem):
                shutil.copy2(caminho_completo_origem, caminho_completo_destino)
                print(f"Copiado: {item} -> {pasta_backup}/")
                
        print("\n[SUCESSO] Backup concluído de forma automática!")

except Exception as e:
    print(f"[ERRO] Ocorreu uma falha ao realizar o backup: {e}")
