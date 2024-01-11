
class Car:

    def __init__(self, name, orientation, row, col, length, color):
        self._name = name # a letter i think
        self._orientation = orientation  # 'H' for horizontal or 'V' for vertical
        self._row = int(row)  # data starts from 1 not 0
        self._col = int(col)  
        self._length = int(length)  # Length of the car (2 or 3 units)

        self._base = [self._row - 1, self._col - 1]

        self._color = color

    def get_color(self):
        return self._color

    def get_rotation(self):
        return [0, 1] if self._orientation == 'H' else [1, 0]

    def get_base(self): 
        return self._base
    
    def get_length(self):
        return self._length

    def get_name(self):
        return self._name
    
    def set_base(self, row, col):
        self._base = [row, col]