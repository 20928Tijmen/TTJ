from CarClass import Car
from typing import Any
import random

'''
This version hardcodes the use of Rushhour6x6_1.csv in add_cars, needs to be in same directory too

'''
class GameBoard:
    def __init__(self, filename):
        self._board = self.get_empty_board(filename)
        self._dictionary_of_cars = {}
        self._car_colors = {}
        self._available_colors = [
    "\033[42m",  # Green
    "\033[43m",  # Yellow
    "\033[44m",  # Blue
    "\033[45m",  # Magenta
    "\033[46m",  # Cyan
    "\033[47m",  # White
    "\033[100m", # Bright Black (Gray)
    "\033[102m", # Bright Green
    "\033[103m", # Bright Yellow
    "\033[104m", # Bright Blue
    "\033[105m", # Bright Magenta
    "\033[106m", # Bright Cyan
    "\033[107m", # Bright White
    "\033[42m",  # Green
    "\033[43m",  # Yellow
    "\033[44m",  # Blue
    "\033[45m",  # Magenta
    "\033[46m",  # Cyan
    "\033[47m",  # White
    "\033[100m", # Bright Black (Gray)
    "\033[102m", # Bright Green
    "\033[103m", # Bright Yellow
    "\033[104m", # Bright Blue
    "\033[105m", # Bright Magenta
    "\033[106m", # Bright Cyan
    "\033[107m", # Bright White
]

    def get_empty_board(self, filename):
        # typehint nodig opeens, niet weghalen
        empty_board: list[list[Any]] = []
        
        if '6x6' in filename:
            loop = 6
        elif '9x9' in filename:
            loop = 9
        elif '12x12' in filename:
            loop = 12

        for ro in range(loop):
            row = []
            for til in range(loop):
                row.append(0)
            empty_board.append(row)

        return empty_board

    def get_board(self):
        return self._board


    def add_cars(self, filename):
        with open(filename) as file:
            next(file)  # Skip the header line
            for line in file:
                name, orientation, col, row, length = line.strip().split(sep=',')

                color = random.choice(self._available_colors)
                self._available_colors.remove(color)

                new_car = Car(name, orientation, row, col, length, color)

                self._dictionary_of_cars[new_car.get_name()] = new_car

                base_row, base_col = new_car.get_base()
                d_row, d_col = new_car.get_rotation()

                for i in range(new_car.get_length()):
                    self._board[base_row + i * d_row][base_col + i * d_col] = new_car.get_name()

    def move_car(self, letter: str, direction):
        car = self._dictionary_of_cars[letter]
        base = car.get_base()
        rotation = car.get_rotation()
        length = car.get_length()

        if direction == 1:
            target_row = base[0] + (rotation[0] * length)
            target_col = base[1] + (rotation[1] * length)
        else: # direction == -1
            target_row = base[0] - rotation[0]
            target_col = base[1] - rotation[1]

        print(base)
        print(target_row)
        print(target_col)
        
        if self._board[target_row][target_col] == 0:

            # Clear the current car
            for i in range(car.get_length()):
                self._board[base[0] + i * rotation[0]][base[1] + i * rotation[1]] = 0

            # Move the car to the new position
            for i in range(car.get_length()):
                new_row = target_row - i * direction * rotation[0]
                new_col = target_col - i * direction * rotation[1]
                self._board[new_row][new_col] = car.get_name()
            
            # Update car's base position
            new_base_row = base[0] + direction * rotation[0]
            new_base_col = base[1] + direction * rotation[1]

            self._dictionary_of_cars[car.get_name()].set_base(new_base_row, new_base_col)

            print(new_base_row)
            print(new_base_col)
            
            print(car.get_base())



    def get_board_for_player(self):
        '''
        this method returns a fancy board with border and background color!
        red car is actually red, exit made clear also

        fancy_board = game.get_board_for_player()
        print(fancy_board) 

        +----+----+----+----+----+----+
        |    |  A |  A |  B |  B |  B |
        +----+----+----+----+----+----+
        
        '''
        board_representation = ""
        # Define background colors
        bg_red = "\033[41m"  # Red background for 'X'
        other_colors = ["\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m"]  # Other colors
        reset_color = "\033[0m"  # Reset color

        # Assign random colors to cars, excluding 'X' and empty spaces
        car_colors = {col: random.choice(other_colors) for row in self._board for col in row if col not in ['X', 0]}

        # Top border
        board_representation += " +" + "----+"*6 + "\n"

        for i, row in enumerate(self._board):
            board_representation += " |"
            for col in row:
                if col == 'X':
                    cell = f"{bg_red}  {col} {reset_color}"
                elif col in self._dictionary_of_cars:
                    car = self._dictionary_of_cars[col]
                    cell = f"{car.get_color()}  {col} \033[0m"
                else:
                    cell = '    '

                board_representation += cell + "|"

            # Border below every line (3rd row longer borders for exit)
            if i == 1 or i == 2: 
                board_representation += "\n +" + "----+"*7 + "\n" 
            else:
                board_representation += "\n +" + "----+"*6 + "\n"

        return board_representation
