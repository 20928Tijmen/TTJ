from GameBoardClass import *
import random

class Algorithm_1():

    def __init__(self, game) -> None:
        """
        Eerste Algoritme: RANDOM

        Pre: Gameboard en History
        """
        self.game = game

        self.cars = list(game._dictionary_of_cars.keys())

    
    def make_random_move(self):
        """
        make a random move
        pre:
        post:
        """
        # choose random car
        random_car = random.choice(self.cars)
        # choose random move
        random_direction = random.choice([1, -1])
        
        return random_car, random_direction


class Algorithm_2():

    def __init__(self, game, letter, direction) -> None:
        """
        Eerste Algoritme: ??

        Pre: Gameboard en History
        """

        self.gameboard = game
        self.letter = letter
        self.direction = direction
    