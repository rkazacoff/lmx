def game_init():
    week_id = 13

    title = ("Home", '\t', 'Away')
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
    games = ""
    games = (title)

    for x in game_list:
        games = games + ('<tr>',x[0], '\t', x[1],'</tr>', '/n')

        print(x)

    #return games

game_init()
#print('\n'.join(str(x) for x in game_list))
#return ('\n'.join(str(x) for x in game_list))
#print (title, '\n'.join(str(x) for x in game_list))

    

#game_init()
