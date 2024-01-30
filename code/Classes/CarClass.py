import random

class Car:
    """
    Represents a car in the Rush Hour game.

    input:
    name: string = the letter representing the car
    orientation: string = either H for horizontal, V for vertical
    row, col: int = the row, col the cars base it at 
    length: int = how many cells long the car is

    Attributes:
        _name (str): Identifier for the car, 1 or 2 letters
        _orientation (str): Orientation of the car, 'H' for horizontal or 'V' for vertical.
        _row (int): The starting row of the car on the game board.
        _col (int): The starting column of the car on the game board.
        _length (int): The length of the car, either 2 or 3.
        _color (str): The assigned color code for terminal display.
        _base (list): The base position [row, col] of the car on the board.
    """


    colors = [
    "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m",
    "\033[100m", "\033[102m", "\033[103m", "\033[104m", "\033[105m", "\033[106m", "\033[107m",
    "\033[48;5;202m", "\033[48;5;220m", "\033[48;5;27m", "\033[48;5;39m", "\033[48;5;90m",
    "\033[48;5;214m", "\033[48;5;226m", "\033[48;5;33m", "\033[48;5;57m", "\033[48;5;69m",
    "\033[48;5;111m", "\033[48;5;128m", "\033[48;5;147m", "\033[48;5;180m", "\033[48;5;213m",
    "\033[48;5;225m", "\033[48;5;240m", "\033[48;5;255m", "\033[48;5;18m", "\033[48;5;66m",
    "\033[48;5;75m", "\033[48;5;102m", "\033[48;5;138m", "\033[48;5;183m", "\033[48;5;55m",
    "\033[48;5;94m", "\033[48;5;123m", "\033[48;5;177m"
]
    
    red =  "\033[48;5;196m"

    reset_color = "\033[0m"  # end the formated string with this to reset the background color


    def __init__(self, name, orientation, row, col, length):
        self._name: str = name
        self._orientation: str = orientation
        self._row: int = int(row)
        self._col: int = int(col)
        self._length: int = int(length)

        self._base: list = [self._row - 1, self._col - 1]

        self._available_colors = self.colors
        self._color = self._set_color()
    
    def _set_color(self):

        if self._name != 'X':
            return random.choice(self._available_colors)
        else:
            return self.red


    def get_color(self):
        """
        Returns the color code of the car for terminal display.
        """
        return self._color

    def get_rotation(self):
        """
        Determines the rotation of the car based on its orientation.
        Returns a list representing the movement in row and column.
        """
        return [0, 1] if self._orientation == 'H' else [1, 0]

    def get_base(self):
        """
        Returns the base position of the car on the board.
        """
        return self._base

    def get_length(self):
        """
        Returns the length of the car.
        """
        return self._length

    def get_name(self):
        """
        Returns the name (identifier) of the car.
        """
        return self._name
    
    def get_name_colored(self) -> str:
        """
        Returns the formated string with backgroundcolor - car name - reset color
        """

        return f"{self._color}{self._name:>3} {self.reset_color}"

    def set_base(self, row, col):
        """
        Sets a new base position for the car.
        """
        self._base = [row, col]

    def reset_base(self):
        """
        Sets the base to [0, 0]
        """
        self._base = [None, None]

    def is_base_set(self):
        """
        Checks if the car's base has been set.
        """
        return self._base[0] is not None and self._base[1] is not None
