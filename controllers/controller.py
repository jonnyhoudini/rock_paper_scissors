from crypt import methods
from flask import render_template, request
from app import app
from models.player import *
from models.game import *

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/play')
def play_computer():
    return render_template('play.html')

@app.route('/game', methods=['POST'])
def play():
    choice_A = request.form['1stplayer']
    choice_B = request.form['2ndplayer']
    player_one = Player("Player 1", choice_A)
    player_two = Player("Player 2", choice_B)
    game = Game()
    winner = game.play_game(player_one, player_two)
    
    return render_template('index.html', player_one=player_one, player_two=player_two, winner=winner)

@app.route('/computer', methods=['POST'])
def computer():
    game = Game()
    player_choice = request.form['1stplayer']
    player_name = request.form['name']
    computer_choice = game.computer_play()
    player = Player(player_name, player_choice)
    computer = Player("The Computer", computer_choice)
    winner = game.play_game(player, computer)

    return render_template('index.html', player_one = player, player_two = computer, winner = winner)
    

    