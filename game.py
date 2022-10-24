from player import HumanPlayer, GeniusComputerPlayer
import time


class TicTacToe:
    def __init__(self):
        self.board = [' ']*9  # we will use a list of length 9 to define 3*3 board
        self.current_winner = None  # we need to keep track of winner

    def print_board(self):
        # this is just getting the rows
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j, j+3)] for j in range(0, 9, 3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # return [i for i, spot in enumerate(self.board) if spot == ' ']
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return len(self.available_moves())
        # return self.board.count(' ')

    def make_move(self, square, letters):
        if self.board[square] == ' ':
            self.board[square] = letters
            if self.winner(square, letters):
                self.current_winner = letters
            return True
        else:
            return False

    def winner(self, square, letters):
        # checking if all 3 symbols in either of 3 rows match
        row_idx = square//3
        row = self.board[row_idx*3: (row_idx+1)*3]
        if all([spot == letters for spot in row]):
            return True

        # checking columns
        col_idx = square % 3
        column = [self.board[col_idx+i*3] for i in range(3)]
        if all([spot == letters for spot in column]):
            return True

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # left to right diagonal
            if all([spot == letters for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # right to left diagonal
            if all([spot == letters for spot in diagonal2]):
                return True

        # if all of these fail
        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letters = 'X'  # starting letter
    while game.empty_squares():
        # get move from appropriate  player
        if letters == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        # defining a function to make move
        if game.make_move(square, letters):
            if print_game:
                print(letters + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letters + ' wins game!')
                return letters
            letters = 'O' if letters == 'X' else 'X'

        # time gap between player and computer to makes things easier to read
        time.sleep(1)

    if print_game:
        print("It\'s a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)