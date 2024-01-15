
class History():
    """
    Must make a history! because you want to be able to record the correct path! and for the algorithm its useful!!
    """
    def __init__(self):
        
        self.move_history: list[(str, int)] = [] # a move is a (letter of car, direction)
        self.board_history: list[list[list]] = [] # the board is a list of lists, so a list of those

        self.counter = 0

    def add_move(self, car_letter: object, direction: int) -> None:
        """
        add a move to the move history
        """
        move = (car_letter, direction)
        self.move_history.append(move)
        self.counter += 1
    
    def add_board(self, board: list[list]) -> list:
        """
        add a board to the board history
        """
        self.board_history.append(board)


    def get_counter(self) -> int:
        """
        returns the counter number
        """
        return self.counter
    
    def get_move_history(self) -> list:
        """
        returns the list of previous moves
        """
        return self.move_history

    def get_board_history(self) -> list:
        """
        return the list of previous boards
        """
        return self.board_history
    
    def go_back(self) -> None:
        """
        makes the last move dissapear of the history and counter
        """
        self.move_history.pop()
        self.counter -= 1
