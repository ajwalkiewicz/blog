# Source: https://swapi.info
import requests

url = "https://swapi.info/api/starships/12"
response = requests.get(url)
starship = response.json()
print(starship["cost_in_credits"] / 1000)