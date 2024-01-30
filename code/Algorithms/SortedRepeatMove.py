import random

class SortedRepeatMove:
    """
    
    """
    def __init__(self, game, history, game_file):
        self.game = game
        self.counter = int(0)

    def make_move(self):
        picked_car = self.game.game_file.get_car_names()[self.counter]
        picked_direction = random.choice([1, -1])
        self.counter += 1
        if self.counter == len(self.game.game_file.get_car_names()):
            self.counter = 0

        return picked_car, picked_direction