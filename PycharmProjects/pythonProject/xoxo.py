class Layer:

    def __init__(self):
        # Initialize the board with spaces indicating available spots
        self.board = [' ' for _ in range(9)]

    def print_board(self):
        # Print the board with current marks
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board_num(self):
        # Print the board with numbers indicating each spot's index
        nums_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in nums_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_move(self):
        moves=[]
        for i,spot in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves


obj=Layer()
obj.print_board_num()