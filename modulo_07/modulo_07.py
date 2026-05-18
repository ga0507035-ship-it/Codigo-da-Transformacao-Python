def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def potencia(base, expoente):
    return base ** expoente

    import utilidades  

    print(f"Soma: {utilidades.somar(10, 5)}")
    print(f"Subtração: {utilidades.subtrair(20, 8)}")
    print(f"Potência: {utilidades.potencia(2, 3)}")

from datetime import date

hoje = date.today()
final_do_ano = date(hoje.year, 12, 31)
faltam = final_do_ano - hoje

print(f"Hoje é dia: {hoje}")
print(f"Faltam {faltam.days} dias para o fim do ano!")

import random
import math

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1
    
    if palpite == numero_secreto:
    
        raiz = math.sqrt(numero_secreto)
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        print(f"Curiosidade: a raiz quadrada do número era {raiz:.2f}")
        break
    elif palpite < numero_secreto:
        print("Mais alto...")
    else:
        print("Mais baixo...")
