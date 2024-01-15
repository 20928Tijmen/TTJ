from CarClass import Car
from GameFileClass import GameFile
from typing import Any


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
            new_car = Car(name, orientation, row, col, length)
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
            target_row = base[0] + (rotation[0] * length)
            target_col = base[1] + (rotation[1] * length)
            if target_row >= len(self._board) or target_col >= len(self._board):
                print("You cannot go there!")
                return False
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

        return True

    
    def make_move_back(self, history):
        """
        this function makes a move where you go back
        """
        # select from the list the last move taken and then its letter
        last_move_letter = history.move_history[-1][0]

        # select from the list the last move taken and then its direction
        last_move_direction = history.move_history[-1][1]

        # make move back in the opposite direction
        if last_move_direction == 1:
            self.move_car(last_move_letter, -1)
        elif last_move_direction == -1:
            self.move_car(last_move_letter, 1)
        else:
            return False

        return True


    def get_board_for_player(self):
        '''
        This method returns a fancy board with border and background color!
        Red car is actually red, exit made clear also.
        Adjusts dynamically to different board sizes.
        '''
        size = int(self.game_file.board_size)
        exit_row = {6: 2, 9: 4, 12: 5}.get(size, 2)

        # Top border
        board = "+" + "----+" * size + "\n"

        for i, row in enumerate(self._board):
            board += "|"
            for col in row:
                if col != 0:
                    car = self._dictionary_of_cars[col]
                    cell = car.get_name_colored() 
                else:
                    cell = '    '
                board += cell + "|"

            # Border below every line (special border for exit row)
            if i == exit_row or i == exit_row - 1:
                board += "\n+" + "----+" * (size + 1) + "\n"  # Longer border for exit
            else:
                board += "\n+" + "----+" * size + "\n"

        return board


    def get_board(self):
        """
        Returns the current state of the game board.
        """
        return self._board

    def get_car_names(self) -> list[str]:
        return list(self._dictionary_of_cars.keys())