import os

from numpy import maximum

path = os.path.dirname(__file__)
input_filename = "pokemon.dat"
output_header = "analysis"
output_hooter = ".csv"
max_namenum = 5
sep = os.linesep

#katakana_list = [chr(i) for i in range(ord("ァ"), ord("ヲ") + 1)]

analysis_list = []
total_analysis = {}

for i in range(max_namenum + 1):
    dict = {}
    #for katakana in katakana_list:
    #    dict[katakana] = 0
    analysis_list.append(dict)

with open(os.path.join(path, input_filename), "r", encoding="utf-8") as pokemon_list:
    for pokemon in pokemon_list:
        for i, char in enumerate(pokemon):
            # 改行や変な文字が入るようなのでその対策
            if char == "\n":
                break
            # ない文字は辞書に登録する
            if not char in analysis_list[i]:
                analysis_list[i][char] = 0
            if not char in total_analysis:
                total_analysis[char] = 0
            analysis_list[i][char] += 1
            total_analysis[char] += 1

def output_file(f, set):
    for char, count in set:
        f.write(char + "," + str(count) + "\n")

total_analysis = sorted(total_analysis.items(), key=lambda x:-x[1])
output_filename = output_header + "0" + output_hooter
with open(os.path.join(path, output_filename), "w", encoding="utf-8_sig") as f:
    output_file(f, total_analysis)

#for i, analysis in enumerate(analysis_list):
for i in range(max_namenum):
    # sorted関数の副作用によって，setに変換される
    analysis = sorted(analysis_list[i].items(), key=lambda x:-x[1])
    output_filename = output_header + str(i+1) + output_hooter
    with open(os.path.join(path, output_filename), "w", encoding="utf-8_sig") as f:
        output_file(f, analysis)