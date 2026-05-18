from faker import Faker

fake = Faker('pt_BR')

print("--- Gerador de Dados Fictícios para Testes ---")

for i in range(1, 4):
    print(f"\nUsuário {i}:")
    print(f"Nome: {fake.name()}")
    print(f"E-mail: {fake.email()}")
    print(f"Cidade: {fake.city()}")
    print(f"Profissão: {fake.job()}")