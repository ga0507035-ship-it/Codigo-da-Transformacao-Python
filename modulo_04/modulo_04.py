lista_compras = []

while True:
    print(f"\nSua lista atual: {lista_compras}")
    print("1. Adicionar item | 2. Remover item | 3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        item = input("Digite o nome do item: ")
        lista_compras.append(item)
    elif opcao == '2':
        item = input("Qual item deseja remover? ")
        if item in lista_compras:
            lista_compras.remove(item)
        else:
            print("Item não encontrado!")
    elif opcao == '3':
        break
    aluno = {
    "nome": "Ricardo",
    "idade": 21,
    "notas": [8.5, 9.0, 7.5]
}

print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Média das notas: {sum(aluno['notas']) / len(aluno['notas']):.2f}")
numeros = [12, 7, 34, 1, 9, 10, 55, 80]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")
agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar | 2. Remover | 3. Buscar | 4. Sair")
    escolha = input("O que deseja fazer? ")

    if escolha == '1':
        nome = input("Nome do contato: ")
        tel = input("Telefone: ")
        agenda[nome] = tel
        print("Contato salvo!")
    
    elif escolha == '2':
        nome = input("Nome para remover: ")
        if nome in agenda:
            del agenda[nome]
            print("Removido com sucesso.")
        else:
            print("Contato inexistente.")

    elif escolha == '3':
        nome = input("Nome para buscar: ")
        print(f"Telefone de {nome}: {agenda.get(nome, 'Não encontrado.')}")

    elif escolha == '4':
        print("Saindo...")
        break
