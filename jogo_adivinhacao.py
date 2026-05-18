import random
import math

print("--- Jogo da Adivinhação ---")
print("Estou pensando em um número entre 1 e 100. Tente adivinhar!")


numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("\nDigite o seu palpite: "))
    tentativas += 1
    
    if chute == numero_secreto:
        print(f"🎯 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas!")
        break
    elif chute < numero_secreto:
        print("Dica: O número secreto é MAIOR.")
    else:
        print("Dica: O número secreto é MENOR.")
        
    diferenca = abs(numero_secreto - chute)
    if diferenca <= 3:
        print("Atenção: Você está QUENTÍSSIMO! Errou por 3 ou menos.")