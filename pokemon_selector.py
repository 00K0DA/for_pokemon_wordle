import os

path = os.path.dirname(__file__)
pokemonlist_file = "pokemon.dat"
pokemon_analysis_header = "analysis"
pokemon_analysis_hooter = ".csv"
max_namenum = 5
output_filename = "pokemonrate.csv"

perfectcollect_rate = 0.2
collect_rate = 0.8

with open(os.path.join(path, pokemonlist_file), "r", encoding="utf-8") as raw_pokemon_list:
    pokemon_list = [d.replace("\n","") for d in raw_pokemon_list]

analysis_list = []
for i in range(max_namenum + 1):
    analysis_filename = pokemon_analysis_header + str(i) + pokemon_analysis_hooter
    with open(os.path.join(path, analysis_filename), "r", encoding="utf-8") as raw_analysis:
        analysis = {}
        for line in raw_analysis:
            line = line.replace("\n","")
            # なぜか最初に入っているので削除する．
            line = line.replace("\ufeff","")
            char, num = line.split(",")
            analysis[char] = int(num)
        analysis_list.append(analysis)

def calculate_pokemonrate(pokemon):
    rate = 0
    existing_char = []
    for i, char in enumerate(pokemon):
        rate += perfectcollect_rate * analysis_list[0][char]
        if not char in existing_char:
            rate += collect_rate * analysis_list[i+1][char]
        existing_char.append(char)
    return rate

pokemonrate_dict = {}
for pokemon in pokemon_list:
    rate = calculate_pokemonrate(pokemon)
    pokemonrate_dict[pokemon] = rate

def output_file(f, set):
    for char, count in set:
        f.write(char + "," + str(count) + "\n")

pokemonrate_set = sorted(pokemonrate_dict.items(), key=lambda x:-x[1])
with open(os.path.join(path, output_filename), "w", encoding="utf-8_sig") as f:
    output_file(f, pokemonrate_set)

