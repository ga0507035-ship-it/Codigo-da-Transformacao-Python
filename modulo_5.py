def saudacao(nome):
    print(f"Olá, {nome}! É um prazer ter você programando conosco.")


saudacao("Gabriel")

def calcular_media(notas):
    media = sum(notas) / len(notas)
    
    if media >= 7:
        situacao = "APROVADO(A)"
    else:
        situacao = "REPROVADO(A)"
        
    print(f"Média: {media:.1f} - Situação: {situacao}")

minhas_notas = [8.5, 6.0, 7.5]
calcular_media(minhas_notas)

def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    return maior, menor

numeros = [10, 5, 20, 1, 15]
v_maior, v_menor = maior_menor(numeros)

print(f"O maior número é {v_maior} e o menor é {v_menor}")

usuarios_db = {
    "admin": "1234",
    "aluno_python": "senha789"
}

def login(usuario, senha):

    if usuario in usuarios_db and usuarios_db[usuario] == senha:
        return True
    else:
        return False


user_input = input("Usuário: ")
pass_input = input("Senha: ")

if login(user_input, pass_input):
    print("Acesso concedido! Bem-vindo ao sistema.")
else:
    print("Acesso negado! Usuário ou senha incorretos.")