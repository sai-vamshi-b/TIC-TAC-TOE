import math
import random

class Player:
    def __init__(self, letters):
        self.letters = letters
        # the chosen side or letter is either X or O

    def get_move(self, game):
        pass


class GeniusComputerPlayer(Player):
    def __init__(self, letters):
        super().__init__(letters)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # get square based off minimax algo
            square = self.minimax(game, self.letters)['position']
        return square

    def minimax(self, state_of_game, player):
        max_player = self.letters  # yourself
        other_player = 'O' if player == 'X' else 'X'  # other player

        # this is a base case
        if state_of_game.current_winner == other_player:
            # we should return position and score because we need to keep track of score for minimax to work
            return {'position': None,
                    'score': 1*(state_of_game.num_empty_squares()+1) if other_player == max_player else
                    -1*(state_of_game.num_empty_squares()+1)
                    }
        elif not state_of_game.num_empty_squares():  # no empty squares
            return {'position': None, 'score': 0}

        # initialize some dictionaries
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize

        for move in state_of_game.available_moves():
            # make move
            state_of_game.make_move(move, player)
            # recurse using minimax to simulate a game after that move
            # we now simulate move of alternate player (here we have to choose the minimum one)
            sim_score = self.minimax(state_of_game, other_player)

            # undo the move
            state_of_game.board[move] = ' '
            state_of_game.current_winner = None
            sim_score['position'] = move  # otherwise this will get messed up from recursion

            # update dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score  # replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # replace best
        return best


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