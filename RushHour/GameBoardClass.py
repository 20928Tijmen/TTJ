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


    def _get_target_location(self, base, rotation, length, direction) -> tuple[int, int]:
        """
        Calculates the target cell for the given car based on its base position, rotation, and move direction.
        """
        if direction == 1:
            target_row = base[0] + (rotation[0] * length)
            target_col = base[1] + (rotation[1] * length)
        else:  # direction == -1
            target_row = base[0] - rotation[0]
            target_col = base[1] - rotation[1]
        return target_row, target_col

    def _legal_move(self, target_row, target_col) -> bool:
        """
        Checks if the move to the target cell is legal.
        """
        if target_row < 0 or target_col < 0 or target_row >= len(self._board) or target_col >= len(self._board[0]):
            return False
        if self._board[target_row][target_col] != 0:
            return False
        return True

    def execute_move(self, car, base, target_row, target_col, direction):
        """
        Executes the car move on the board.
        """
        for i in range(car.get_length()):
            self._board[base[0] + i * car.get_rotation()[0]][base[1] + i * car.get_rotation()[1]] = 0

        for i in range(car.get_length()):
            new_row = target_row - i * direction * car.get_rotation()[0]
            new_col = target_col - i * direction * car.get_rotation()[1]
            self._board[new_row][new_col] = car.get_name()

        car.set_base(target_row, target_col)


    def move_car(self, letter: str, direction: int):
        """
        Moves the car in the specified direction if the move is legal.
        """
        car = self._dictionary_of_cars[letter]
        base = car.get_base()
        rotation = car.get_rotation()
        length = car.get_length()

        target_row, target_col = self._get_target_location(base, rotation, length, direction)

        if not self._legal_move(target_row, target_col):
            print("Illegal move. Please try again.")
            return
        
        print(target_row, target_col)

        self.execute_move(car, base, target_row, target_col, direction)

    
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
