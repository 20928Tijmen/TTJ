from GameBoardClass import GameBoard
from typing import Any

class History():
    """
    Must make a history! because you want to be able to record the correct path! and for the algorithm its useful!!
    """
    def __init__(self):
        
        self.states_history: list[Any] = []
        self.counter = 0

    def add_move(self, car: object, direction: int):
        """
        add a move to the history
        """
        move = (car, direction)
        self.states_history.append(move)
        self.counter += 1

    def show_counter(self):
        """
        shows the counter number
        """
        return self.counter
    
    def show_states_history_list(self):
        """
        shows the list of moves made
        """
        return self.states_history
    
    def go_back(self):
        """
        makes the last move dissapear of the list and counter
        """
        self.states_history.pop()
        self.counter -= 1
