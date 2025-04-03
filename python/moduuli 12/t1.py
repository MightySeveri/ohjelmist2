import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    vitsi = data["value"]

print(vitsi)