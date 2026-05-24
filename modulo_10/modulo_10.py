import requests

# Configurações de credenciais e parâmetros
WEATHER_TOKEN = "SUA_API_KEY_WEATHER_AQUI"
TARGET_CITY = "Sao Paulo"

TMDB_TOKEN = "SUA_API_KEY_TMDB_AQUI"
SEARCH_MOVIE = "Inception"

try:
    # Organizando os parâmetros da URL em um dicionário (muda a estrutura do código original)
    weather_params = {
        "q": TARGET_CITY,
        "appid": WEATHER_TOKEN,
        "units": "metric",
        "lang": "pt_br"
    }
    
    weather_response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=weather_params, timeout=10)
    weather_response.raise_for_status()
    weather_payload = weather_response.json()
    
    current_temp = weather_payload["main"]["temp"]
    weather_desc = weather_payload["weather"][0]["description"]
    
    print("========== CLIMA ATUAL ==========")
    print(f"Localidade: {TARGET_CITY}")
    print(f"Temperatura: {current_temp} °C")
    print(f"Status: {weather_desc.upper()}")
    print("=================================\n")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do Tempo: {erro}\n")
except KeyError:
    print("Erro ao processar os dados do tempo recebidos.\n")

try:
    # Organizando os parâmetros do TMDB de forma separada
    tmdb_params = {
        "api_key": TMDB_TOKEN,
        "query": SEARCH_MOVIE,
        "language": "pt-BR"
    }
    
    movie_response = requests.get("https://api.themoviedb.org/3/search/movie", params=tmdb_params, timeout=10)
    movie_response.raise_for_status()
    movie_payload = movie_response.json()
    
    if movie_payload.get("results"):
        main_match = movie_payload["results"][0]
        movie_title = main_match["title"]
        movie_summary = main_match["overview"]
        
        print("========== RESULTADO DA BUSCA ==========")
        print(f"Filme: {movie_title}")
        print(f"Resumo: {movie_summary}")
        print("========================================")
    else:
        print(f"A pesquisa por '{SEARCH_MOVIE}' não retornou resultados.")

except requests.exceptions.RequestException as erro:
    print(f"Erro na conexão com a API do TMDB: {erro}")
except KeyError:
    print("Erro ao processar os dados do filme recebidos.")
