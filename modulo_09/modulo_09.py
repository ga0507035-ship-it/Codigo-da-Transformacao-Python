import requests

API_KEY = "SUA_API_KEY_AQUI"
CIDADE = "Sao Paulo"
URL_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(URL_WEATHER, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()
    
    temperatura = dados["main"]["temp"]
    descricao = dados["weather"][0]["description"]
    
    print(f"Cidade: {CIDADE}")
    print(f"Temperatura atual: {temperatura}°C")
    print(f"Condição climática: {descricao.capitalize()}")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API: {erro}")
except KeyError:
    print("Erro ao processar os dados recebidos.")
