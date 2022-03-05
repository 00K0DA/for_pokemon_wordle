import requests
from bs4 import BeautifulSoup
import re
import os
import codecs

input_url = "https://yakkun.com/dp/zukan/"
output_path = os.path.dirname(__file__)
output_filename = "pokemon.dat"
#sep = os.linesep
sep = "\n"

response = requests.get(input_url)
response.encoding = response.apparent_encoding
data = response.text
soup = BeautifulSoup(data, 'html.parser')
pokemon_scrolldown = soup.find("select", id="no", class_="space")
raw_pokemon_list = pokemon_scrolldown.findAll('option')
pokemon_list = [d.string for d in raw_pokemon_list]

pokemon_regex = re.compile(r'(\d{3}): (.{2,5})')

with open(os.path.join(output_path, output_filename), "w", encoding='utf-8') as f:
    for pokemon in pokemon_list:
        result = pokemon_regex.search(pokemon)
        pokemon_id = result.group(1)
        pokemon_name = result.group(2)
        if len(pokemon_name) == 5:
           f.write(pokemon_name + sep)