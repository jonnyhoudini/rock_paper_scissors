import random

class Game():

    # def __init__(self, player_one, player_two):
    #     self.player_one = player_one
    #     self.player_two = player_two

    def play_game(self, player_one, player_two):
            if player_one.choice == 'rock' and player_two.choice == 'paper':
                return player_two
            elif player_one.choice == 'paper' and player_two.choice == 'rock':
                return player_one
            elif player_one.choice == 'scissors' and player_two.choice == 'rock':
                return player_two
            elif player_one.choice == 'rock' and player_two.choice == 'scissors':
                return player_one
            elif player_one.choice == 'paper' and player_two.choice == 'scissors':
                return player_two
            elif player_one.choice == 'scissors' and player_two.choice == 'paper':
                return player_one
            else: 
                return None

    def get_result(self):
        result = self.play_game()
        if result == None:
            return "It's a draw"
        else:
            return f"{result.name} is the winner"

    def computer_play(self):
        list = ["rock", "paper", "scissors"]
        computer_choice = random.choice(list)
        return computer_choice