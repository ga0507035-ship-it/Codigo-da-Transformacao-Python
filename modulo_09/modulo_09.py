def calculadora_divisao():
    print("--- CALCULADORA DE DIVISÃO ---")
    try:
        # Tenta converter as entradas para números decimais
        numerador = float(input("Digite o primeiro número (dividendo): "))
        denominador = float(input("Digite o segundo número (divisor): "))
        
        resultado = numerador / denominador
        print(f"Resultado: {numerador} / {denominador} = {resultado}")
        
    except ZeroDivisionError:
        print("Erro: Não é possível realizar uma divisão por zero.")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")

# Para testar a calculadora:
if __name__ == "__main__":
    calculadora_divisao()
    # Criando a exceção personalizada herdeira da classe base Exception
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.message = f"Saldo insuficiente! Tentativa de sacar R${valor_saque:.2f}, mas o saldo é de R${saldo_atual:.2f}."
        super().__init__(self.message)


class ContaBancaria:
    def __init__(self, titular: str, idade_titular: int, saldo_inicial: float = 0.0):
        # Validação de idade (Atividade 3)
        if idade_titular <= 0:
            raise ValueError("A idade do titular precisa ser um número positivo maior que zero.")
        if idade_titular < 18:
            print("Aviso: Titular menor de idade cadastrado com sucesso.")
            
        self.titular = titular
        self.idade = idade_titular
        self.saldo = saldo_inicial

    def sacar(self, valor: float):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return

        # Lançando a exceção caso falte saldo (Atividade 2)
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado! Novo saldo: R${self.saldo:.2f}")


# --- TESTANDO O SISTEMA BANCÁRIO ---
if __name__ == "__main__":
    print("\n--- Teste do Sistema Bancário ---")
    
    # 1. Testando a validação de idade (descomente para testar o erro)
    
    # conta_erro = ContaBancaria("Carlos", -5, 100.0)
    
    try:
        minha_conta = ContaBancaria("Mariana", 24, 150.0)
        print(f"Conta de {minha_conta.titular} criada com sucesso.")
        
        # Tentando realizar um saque válido
        minha_conta.sacar(50.0)
        
        # Tentando realizar um saque que estoura o saldo (força o erro)
        minha_conta.sacar(200.0)
        
    except SaldoInsuficienteError as erro:
        print(f"Exceção capturada -> {erro}")
    except ValueError as erro:
        print(f"Erro de validação -> {erro}")def sistema_login():
    # Credenciais registradas no banco de dados fictício
    USUARIO_CORRETO = "admin"
    SENHA_CORRETA = "senha123"
    
    tentativas_restantes = 3
    print("\n--- SISTEMA DE LOGIN ---")
    
    while tentativas_restantes > 0:
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()
        
        try:
            # Se tudo estiver correto, encerra a função
            if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
                print("\nLogin bem-sucedido! Bem-vindo de volta.")
                return
            else:
                # Se algo estiver errado, lança um erro de valor
                raise ValueError("Usuário ou senha incorretos.")
                
        except ValueError as erro:
            tentativas_restantes -= 1
            print(f"{erro} Tentativas restantes: {tentativas_restantes}\n")
            
    print("Acesso bloqueado! Você excedeu o número máximo de tentativas.")

# Para testar o login:
if __name__ == "__main__":
    sistema_login()
