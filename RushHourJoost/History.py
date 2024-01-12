from GameBoardClass import GameBoard

class History():
    def __init__(self):
        
        self.states_history: list[Any] = []
        self.counter = 0

    def add_move(self, car: object, direction: int):
        """
        add a move to the history
        """
        move = (car, direction)
        self.states_history.append(move)
        self.counter + 1

    def show_counter(self):
        return self.counter
        
    

"""
Must make a history! because you want to be able to record the correct path! and for the algorithm its useful!!
"""




from typing_extensions import Self
from typing import Any

class History(object):

    def __init__(self: Self) -> None:
        """
        post: creates an empty LIFO stack
        """
        self.rooms_history: list[Any] = []
    
    def add_room(self: Self, x: object) -> None:
        """post: places x on top of the stack"""
        self.rooms_history.append(x)

    def move_back(self: Self) -> Any:
        """pre: self.size O > 0
        post: removes and returns the top element of
        the stack"""
        return self.rooms_history.pop()
    
    def size(self: Self) -> int:
        """post: returns the number of elements in the stack"""
        return len(self.rooms_history)