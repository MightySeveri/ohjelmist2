import requests

kaupunki = input("syötä kaupunki")
API_KEY = "36dcb8c406aea8c484388ae786fa5111"
url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={API_KEY}&units=metric"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
print(f"Sää {kaupunki} kaupungissa: {data['weather'][0]['description']}")
print(f"lämpötila: {data ['main']['temp']} C")