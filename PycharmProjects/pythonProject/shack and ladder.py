import random
from time import sleep

class snack_lasdder:
    def __init__(self):
        self.ladder ={1:38,4:14,8:30,21:42,28:74,50:67,71:92,88:99}
        self.snake= {36:6,32:10,62:18,88:24,48:26,95:56,97:78}
        self.num_player = int(input("enter the no of players: "))
        self.position = [0]*self.num_player
        self.started = [False] * self.num_player

    @staticmethod
    def print_board():
        print()
        fmt = '|{:4} ||{:4} ||{:4} ||{:4} ||{:4} ||{:4} ||{:4} ||{:4} ||{:4} ||{:4} |'
        separate = "_"*60
        for i in range(0,101,10):
            print(fmt.format(i,i+1,i+2,i+3,i+4,i+5,i+6,i+7,i+8,i+9))
            print(separate)

    @staticmethod
    def Dice():
        input("press enter to roll Dice...")
        sleep(0.3)
        return random.randint(1,6)
    def player(self):
           while True:
                for i in range(self.num_player):
                    print(f"\nPlayer {i + 1}'s turn:")
                    if not self.started[i]:
                        roll = 0
                        while roll != 1:
                            roll = self.Dice()
                            print(F"rolled: {roll} new current{self.position} ")
                            if roll == 1:
                                self.started[i] = True
                                print(" you can start move now ")
                    else:
                        roll = self.Dice()
                        self.position[i] += roll
                        print(f"Rolled: {roll}, Current Position: {self.position[i]}")

                        if self.position[i] in self.ladder:
                            self.position[i] = self.ladder[self.position[i]]
                            print(f"Ladder!🪜 Move up {self.position[i]}")

                        if self.position[i] in self.snake:
                            self.position[i] = self.snake[self.position[i]]
                            print(f"Snake🐍 Move down  {self.position[i]}")

                        if self.position[i] > 100:
                            self.position[i] -= roll
                            print("Roll exceeded 100 😐😐😐 Try again")

                        if self.position[i] == 100:
                            print(f"Congratulations  {i + 1}, you won!")
                            return




game = snack_lasdder()
game.print_board()
game.player()