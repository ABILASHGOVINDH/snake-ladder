import math
import random
class player:
    def __init__(self,letter):
        self.letter = letter
    def get_move(self,game):
        pass

class random_computer_player(player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_move())
        return square
class Human_player(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = True
        val = None
        while  valid_square:
            square = input(self.letter + " input move(0-8)")

            try:
                val = int(square)
                if val not in game.available_move():
                    raise ValueError
                valid_square = False
            except ValueError:
                print("Invalid  syntax error! ")

        return val

