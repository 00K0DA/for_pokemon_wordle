# for_pokemon_wordle
ポケモンwordleにおいて，最初のポケモンに何を指定したら良いかを計算するプログラムです．
https://wordle.mega-yadoran.jp/

pokemon_collecor.pyを実行すると，第4世代以前の5文字のポケモンをリストアップしたpokemon.datが生成されます．
  
    ポケモン名は，ポケモン徹底攻略様より取得しています．
  
    (https://yakkun.com/dp/zukan/)

pokemon_analyzer.pyを実行すると，analysis0-5.csvが生成されます．

    analysis0.csv：ポケモン名にその文字が使われた回数の合計を，文字ごとに降順で格納したcsvファイル

    analysis1-4.csv：ポケモン名のn番目にその文字が使われた回数の合計を，文字ごとに降順で格納したcsvファイル

pokemon_selector.pyを実行すると，pokemonrate.csvが生成されます．

    pokemonrate.csvファイルは，各ポケモンの点数を降順に格納しています．
    
    各ポケモンの点数は，以下の手順で計算します．
    
        1. 文字・位置ともに合っていた場合，「その文字が使われた回数×重み1」を加算する．
        
        2. 文字が合っていて，かつその文字が2回以上使われていなければ「n文字目にその文字が使われた回数×重み2」を加算する．
        
        3. 1,2の手順を，点数を計算したいポケモンの文字それぞれに適用する．
        
    重み1はperfectcollect_rate, 重み2はcollect_rateという変数で保存しているので，比を変えたい場合はプログラムを編集してください．
    
    現在，perfectcollect_rate = 0.2，collect_rate=0.8で計算しています．
