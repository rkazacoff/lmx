markup = """
<!doctype html>
<html>
    <head>
        <title>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""
game_1 = ["Veracruz", "Atlas"]
game_2 = ["Puebla", "Monarcas"]
game_3 = ["Cruz Azul", "Queretaro"]
game_4 = ["Leon", "Necaxa"]
game_5 = ["Tigres", "Pumas"]
game_6 = ["Chivas", "BUAP"]
game_7 = ["Tijuana", "America"]
game_8 = ["Toluca", "Monterey"]
game_9 = ["Santos", "Pachuca"]
game_list = [game_1, game_2, game_3, game_4,game_5,game_6,game_7,game_8,game_9]

markup = markup 

for x in game_list:
    markup = markup + x[0] + x[1] 

markup = markup +"""
        </h1> 
    </body> 
</html>"""
    
print(markup)
