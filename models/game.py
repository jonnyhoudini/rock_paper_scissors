class Game():

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    # def play_game(self):
    #     if self.player_one.choice == 'rock' and self.player_two.choice == 'paper':
    #         return f"{self.player_two.name} is the winner"
    #     elif self.player_one.choice == 'paper' and self.player_two.choice == 'rock':
    #         return f"{self.player_one.name} is the winner"
    #     elif self.player_one.choice == 'scissors' and self.player_two.choice == 'rock':
    #         return f"{self.player_two.name} is the winner"
    #     elif self.player_one.choice == 'rock' and self.player_two.choice == 'scissors':
    #         return f"{self.player_one.name} is the winner"
    #     elif self.player_one.choice == 'paper' and self.player_two.choice == 'scissors':
    #         return f"{self.player_two.name} is the winner"
    #     elif self.player_one.choice == 'scissors' and self.player_two.choice == 'paper':
    #         return f"{self.player_one.name} is the winner"
    #     else: 
    #         return "It's a draw"

    def play_game(self):
            if self.player_one.choice == 'rock' and self.player_two.choice == 'paper':
                return self.player_two
            elif self.player_one.choice == 'paper' and self.player_two.choice == 'rock':
                return self.player_one
            elif self.player_one.choice == 'scissors' and self.player_two.choice == 'rock':
                return self.player_two
            elif self.player_one.choice == 'rock' and self.player_two.choice == 'scissors':
                return self.player_one
            elif self.player_one.choice == 'paper' and self.player_two.choice == 'scissors':
                return self.player_two
            elif self.player_one.choice == 'scissors' and self.player_two.choice == 'paper':
                return self.player_one
            else: 
                return None

    def get_result(self):
        result = self.play_game()
        if result == None:
            return "It's a draw"
        else:
            return f"{result.name} is the winner"