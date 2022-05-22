from crypt import methods
from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/game', methods=['POST'])
def play():
    choice_A = request.form['1stplayer']
    choice_B = request.form['2ndplayer']
    player_one = Player("Player 1", choice_A)
    player_two = Player("Player 2", choice_B)
    game = Game(player_one, player_two)
    winner = game.play_game()
    
    return render_template('index.html', player_one=player_one, player_two=player_two, winner=winner)

@app.route('/computer', methods=['POST'])
def computer():
    choice_A = request.form['1stplayer']
    