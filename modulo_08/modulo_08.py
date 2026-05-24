class Carro:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_info(self):
        """Imprime as informações básicas do veículo."""
        print(f"Carro: {self.marca} {self.modelo}")

    def __str__(self):
        """Retorna uma representação em texto personalizada do objeto."""
        return f"{self.marca} {self.modelo}"


# Implementando a Herança (Atividade 2)
class CarroEletrico(Carro):
    def __init__(self, marca: str, modelo: str, autonomia_bateria: int):
        # O super() puxa os atributos da classe mãe (Carro)
        super().__init__(marca, modelo)
        self.autonomia_bateria = autonomia_bateria  # Atributo exclusivo

    def exibir_info(self):
        """Sobrescreve o método para incluir a autonomia da bateria."""
        print(f"Carro Elétrico: {self.marca} {self.modelo} | Autonomia: {self.autonomia_bateria}km")

    def __str__(self):
        """Retorna a representação em texto do carro elétrico."""
        return f"{self.marca} {self.modelo} (Elétrico) - {self.autonomia_bateria}km de autonomia"


# --- TESTANDO AS CLASSES 1, 2 e 3 ---
if __name__ == "__main__":
    print("--- Teste de Carros ---")
    # Criando um carro normal
    meu_carro = Carro("Toyota", "Corolla")
    meu_carro.exibir_info()
    print(f"Usando o __str__: {meu_carro}\n")

    # Criando um carro elétrico
    meu_eletrico = CarroEletrico("BYD", "Dolphin", 400)
    meu_eletrico.exibir_info()
    print(f"Usando o __str__: {meu_eletrico}\n")
