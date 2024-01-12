
class Car:
    """
    Represents a car in the Rush Hour game.

    Attributes:
        _name (str): Identifier for the car, 1 or 2 letters
        _orientation (str): Orientation of the car, 'H' for horizontal or 'V' for vertical.
        _row (int): The starting row of the car on the game board.
        _col (int): The starting column of the car on the game board.
        _length (int): The length of the car, either 2 or 3.
        _color (str): The assigned color code for terminal display.
        _base (list): The base position [row, col] of the car on the board.
    """
    def __init__(self, name, orientation, row, col, length, color):
        self._name = name
        self._orientation = orientation
        self._row = int(row)
        self._col = int(col)
        self._length = int(length)
        self._color = color
        self._base = [self._row - 1, self._col - 1]

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

    def set_base(self, row, col):
        """
        Sets a new base position for the car.
        """
        self._base = [row, col]
