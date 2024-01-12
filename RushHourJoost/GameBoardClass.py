from CarClass import Car
from GameFileClass import GameFile
from typing import Any
import random


class GameBoard:
    """
    Represents the game board for Rush Hour.

    Attributes:
        game_file (GameFile): The game file containing board information.
        _car_colors (dict): A dictionary to store colors for each car.
        _available_colors (list): A list of available color codes for cars.
        _dictionary_of_cars (dict): A dictionary mapping car names to Car objects.
        _board (list): The game board, a 2D list representing the grid.
    """

    def __init__(self, game_file):

        self.game_file = game_file

        self._car_colors = {}
        self._available_colors = [
            "\033[42m", "\033[43m", "\033[44m", "\033[45m", "\033[46m", "\033[47m",
            "\033[100m", "\033[102m", "\033[103m", "\033[104m", "\033[105m", "\033[106m", "\033[107m",
        ]

        self._dictionary_of_cars = self._create_cars()
        self._board = self._create_empty_board()

        self._place_cars()


    def _create_empty_board(self):
        """
        Creates an empty board based on the size specified in the game file.
        """
        size = int(self.game_file.board_size)
        return [[0 for _ in range(size)] for _ in range(size)]


    def _create_cars(self):
        """
        Creates Car objects based on information in the game file.
        """
        car_dict = {}
        for name, orientation, row, col, length in self.game_file.car_info:
            color = random.choice(self._available_colors)
            new_car = Car(name, orientation, row, col, length, color)
            car_dict[new_car.get_name()] = new_car
        return car_dict


    def _place_cars(self):
        """
        Places cars on the board based on their base position and orientation.
        """
        for name, car in self._dictionary_of_cars.items():
            base_row, base_col = car.get_base()
            d_row, d_col = car.get_rotation()

            for i in range(car.get_length()):
                self._board[base_row + i * d_row][base_col + i * d_col] = name


    def move_car(self, letter: str, direction):
        car = self._dictionary_of_cars[letter]
        base = car.get_base()
        rotation = car.get_rotation()
        length = car.get_length()        

        if direction == 1:
            if (base[1] + length) >= len(self._board) or (base[0] + length) >= len(self._board):
                print("You cannot go there!")
                return False
            target_row = base[0] + (rotation[0] * length)
            target_col = base[1] + (rotation[1] * length)
        elif direction == -1:
            target_row = base[0] - rotation[0]
            target_col = base[1] - rotation[1]
        else:
            print("Invalid move!")
            return False
        
        if self._board[target_row][target_col] != 0 or target_col < 0 or target_row < 0:
            print("You cannot go there!")
            return False

        elif self._board[target_row][target_col] == 0:
            
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


    def get_board_for_player(self):
        '''
        This method returns a fancy board with border and background color!
        Red car is actually red, exit made clear also.
        Adjusts dynamically to different board sizes.
        '''
        # Define background colors
        bg_red = "\033[41m"  # Red background for 'X'
        reset_color = "\033[0m"  # Reset color

        size = int(self.game_file.board_size)

        exit_row = {6: 2, 9: 4, 12: 5}.get(size, 2)

        # Top border
        board_representation = "+" + "----+" * size + "\n"

        for i, row in enumerate(self._board):
            board_representation += "|"
            for col in row:
                if col == 'X':
                    cell = f"{bg_red}{col:>3} {reset_color}"
                elif col != 0:
                    cell = f"{self._dictionary_of_cars[col].get_color()}{col:>3} {reset_color}"
                else:
                    cell = '    '
                board_representation += cell + "|"

            # Border below every line (special border for exit row)
            if i == exit_row or i == exit_row - 1:
                board_representation += "\n+" + "----+" * (size + 1) + "\n"  # Longer border for exit
            else:
                board_representation += "\n+" + "----+" * size + "\n"

        return board_representation


    def get_board(self):
        """
        Returns the current state of the game board.
        """
        return self._board