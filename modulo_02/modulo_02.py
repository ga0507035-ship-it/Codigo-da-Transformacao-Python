
print("Olá, Jovem!")


print(type(10))        # Saída: <class 'int'>
print(type("Texto"))   # Saída: <class 'str'>

from datetime import datetime

nome = input("Qual é o seu nome? ")

agora = datetime.now()
hora_formatada = agora.strftime("%H:%M")


print(f"Olá, {nome}! Seja bem-vindo(a).")

print(f"Agora são exatamente {hora_formatada}.")
