# PASO NUMERO1 #
import requests
# URL de l'API per obtenir les categories
url = "https://api.chucknorris.io/jokes/categories"
# Executar la petició GET
response = requests.get(url)


# Comprovar el codi d'estat
if response.status_code == 200:  # 200 OK indica que la petició ha estat exitosa
    print("✅ Èxit!")
    # response.text conté el Body (cos de la resposta)
    print(response.text)
else:
    # Capturar errors del client (4xx) o del servidor (5xx)
    print(f"❌ Error {response.status_code}")

# PASO NUMERO2A #
import requests

# URL amb el paràmetre integrat
url = "https://api.chucknorris.io/jokes/random?category=food"

response = requests.get(url)

if response.status_code == 200:
    print("✅ Èxit!")
    print(response.text)
else:
    print(f"❌ Error {response.status_code}")

# PASO NUMERO2B #
import requests

url = "https://api.chucknorris.io/jokes/random"
# Els paràmetres (Query params) es passen com un diccionari
params = {"category": "food"}

response = requests.get(url, params=params)

# La propietat response.url mostra la URL final generada
print(response.url)
print("✅ Resposta JSON:")
# response.json() converteix el cos de la resposta (Body) en un diccionari Python
print(response.json())