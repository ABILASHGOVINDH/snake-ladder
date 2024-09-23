from player import Human_player,random_computer_player

class TicTacToa:
    def __init__(self):
        self.bord = [" " for _ in range(9)]
        self.current_winner =None

    def print_bord(self):
         for row in [self.bord[i*3:(i+1)*3] for i in range(3)]:
             print("| "+ " | ".join(row)+ " |")
    @staticmethod
    def print_bord_nums():
        for i in range(0, 9, 3):
            print(f"|{i} | {i + 1} |  {i + 2} |")
    def available_move(self):
         return [i for i, x in enumerate(self.bord) if x == " "]
         # move = []
         # for i,spot in enumerate(self.bord):
         #     if spot == ' ':
         #         move.append(i)
         # return move
    def empty_square(self):
        return " " in self.bord
    def nums_square(self):
        return self.bord.count(" ")
    def make_move(self,square,letter):
        if self.bord[square] == ' ':
            self.bord[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self,square,letter):
        row_ind = square// 3
        row = self.bord[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        row  = [self.bord[col_ind+i*3] for i in range(3)]
        if all( [column == letter for column in row]):
            return True
        if square %2 == 0:
              diagonal_i = [self.bord[i] for i in [0,4,8]]
              if all([spot == letter for spot in diagonal_i]):
                  return True
              diagonal_ii = [self.bord[i] for i in [2,4,6]]
              if all([spot == letter for spot in diagonal_ii]):
                 return True
        return False

def play(game,x_player,o_player,print_game = True):
    if print_game:
        game.print_bord_nums()

        letter = 'X'
        while game.empty_square():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter, f'makes a move to square {square}')
                    game.print_bord()
                    print(' ')
                if game.current_winner:
                    if print_game:
                       print(letter," you won!!")
                    return letter

                letter = "O" if letter == "X" else "X"
        if print_game:
                print("It's a tie")


if __name__ == "__main__":
    x_player = Human_player("X")
    o_player = random_computer_player("O")
    t = TicTacToa()
    play(t, x_player, o_player, print_game=True)