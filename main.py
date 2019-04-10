from flask import Flask
from format import game_init

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return game_init()
       
    


app.run()