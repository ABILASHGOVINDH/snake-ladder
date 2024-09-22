iiimport queue

avina@Abee MINGW64 ~/PycharmProjects/pythonProject (master)
$ cat
clear
clear
import sys
import random


class Node:
    def __init__(self,row,col):
        self.row =row
        self.col =col

class SnakeGame:
     def __init__(self,row,col):
         self.col = col
         self.row = row
         self.board = [[" " for _ in range(col+2)] for _ in range(row+2)]
         self.snake_queue = queue.Queue()
         self.food_queue = queue.Queue()

         for r in range(row + 2):
             self.board[r][0] = "|"
             self.board[r][col + 1] = "|"
         for c in range(col + 2):
             self.board[0][c] = "_"
             self.board[row + 1][c] = "_"

         self.snake_queue.put(Node(1,1))

         food_postion = [(random.randint(1,row),random.randint(1,col)) for _ in range(5)]
         for pos in food_postion:
             self.food_queue.put(Node(pos[0],pos[1]))
         self.display(self.food_queue.get())
         option = input(" do u wanna play this game chose {Y/N}: ").strip().upper()
         if option == "Y":
             self.snake_move(1,1)
         else:
             sys.exit()
     def snake_move(self,row,col):
             if 1 <= row <= self.row and 1 <= col <= self.col:
                 if self.board[row][col] == ".":
                     print("Game Over")
                     return False
                 if self.board[row][col] != "X":
                     tail = self.snake_queue.get()
                     self.board[tail.row][tail.col] = " "
                 if self.board[row][col] == "X":
                     if self.food_queue.empty():
                         print("Game OVer!!!")
                         return False
                     self.display(self.food_queue.get())
                 self.snake_queue.put(Node(row,col))
                 self.move_print(row,col)

                 direction = input("Enter a move ⬆️⬇️⬅️➡️ (U/D/L/R): ").strip().upper()
                 if direction == "U":
                     return self.snake_move(row - 1, col)
                 elif direction == "D":
                     return self.snake_move(row + 1, col)
                 elif direction == "L":
                     return self.snake_move(row, col - 1)
                 elif direction == "R":
                     return self.snake_move(row, col + 1)
                 else:
                     print("invalid syntax ")
                     return False
             else:
                 print("Direction invalid ")
                 return False

     def display(self,node):
         self.board[node.row][node.col] = "X"


     def move_print(self,row,col):
         self.board[row][col] = "."
         self.print_board()

     def print_board(self):
         for row in self.board:
             print("".join(row))


game = SnakeGame(10,10)
game.snake_move(1,1)

