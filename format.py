def game_init():
    markup = """
    
    <!doctype html>
    <html>
        <head>
            <table>
                
                <td>{0}</td>
                <td>{1}</td>
            </table>
        </head>
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

    markup_final = '<th>Home    Visitante</th>'

    for x in game_list:
        markup_final += markup.format(x[0], x[1]) 
    return markup_final
# markup = markup +"""
#         </h1> 
#     </body> 
# </html>"""
    
# print(markup)