
print("=== Bem-vindo à Calculadora Python ===")

while True:
    print("\nOperações disponíveis:")
    print(" + : Soma")
    print(" - : Subtração")
    print(" * : Multiplicação")
    print(" / : Divisão")
    print(" S : Sair")

   
    operacao = input("\nEscolha a operação: ").strip().upper()

    if operacao == 'S':
        print("Encerrando a calculadora... Até logo!")
        break  # Estrutura de repetição: interrompe o loop

    if operacao in ('+', '-', '*', '/'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 != 0:
                    resultado = num1 / num2
                else:
                    resultado = "Erro! Divisão por zero não permitida."

            print(f"\n>>> Resultado: {resultado}")
            
        except ValueError:
            print("Erro: Por favor, digite apenas números válidos.")
    else:
        print("Operação inválida! Tente novamente.")