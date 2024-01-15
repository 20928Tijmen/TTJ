from GameBoardClass import *
import random

class Algorithm_1():

    def __init__(self, game, letter, direction) -> None:
        """
        Eerste Algoritme: RANDOM

        Pre: Gameboard en History
        """

        self.game = game
        self.letter = letter
        self.direction = direction

        while game.iswon() is False:
            self.make_random_move()
    
    def make_random_move(letter, direction):
        """
        make a random move
        pre:
        post:
        """
        # choose random car
        letter = random()
        # choose random move
        direction = random()






class Algorithm_2():

    def __init__(self, game, letter, direction) -> None:
        """
        Eerste Algoritme: ??

        Pre: Gameboard en History
        """

        self.gameboard = game
        self.letter = letter
        self.direction = direction
    