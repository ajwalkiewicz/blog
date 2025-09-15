# Source: https://swapi.info/starships/12
from typing import cast

import requests

url = "https://swapi.info/api/starships/12"
response = requests.get(url)
starship = cast(dict[str, str], response.json())
print(starship["model"].upper()) # Outputs: T-65 X-WING