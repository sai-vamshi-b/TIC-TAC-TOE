class TicTacToe:
    def __init__(self):
        self.board = [' ']*9  # we will use a list of length 9 to define 3*3 board
        self.current_winner = None  # we need to keep track of winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i:i+3] for i in range(0,9,3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_number(self):
        # 0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j,j+3)] for j in range(0,9,3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot)  in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        # return self.board.count(' ')

    def make_move(self, square, oorx):
        if self.board[square] == ' ':
            self.board[square] = oorx
            return True
        else:
            return False


def play(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    oorx = 'X' # starting letter
    while game.empty_squares():
        # get move from appropriate  player
        if oorx == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # defining a function to make move
        if game.make_move(square, oorx):
            if print_game:
                print(oorx + f' makes a move to square {square}')
                game.print_board()
                print('')

            oorx = 'O' if oorx == 'X' else 'O'