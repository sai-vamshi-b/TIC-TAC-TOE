# import math
import random


class Player:
    def __init__(self, letters):
        self.letters = letters
        # the chosen side or letter is either X or O

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letters):
        super().__init__(letters)

    def get_move(self, game):
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letters):
        super().__init__(letters)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letters + '\'s turn. Input move from (0-8):')
            # we're going to return invalid as answer either
            # if the value is not an integer or
            # if the range is out of board or spot is unavailable
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


