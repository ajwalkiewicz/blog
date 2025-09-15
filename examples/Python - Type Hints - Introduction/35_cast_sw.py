# Source: https://swapi.info
from typing import cast
import requests

url = "https://swapi.info/api/starships/12"
response = requests.get(url)
starship = cast(dict[str, str], response.json())
starship: dict[str, str] = response.json()
print(starship["cost_in_credits"] / 1000)