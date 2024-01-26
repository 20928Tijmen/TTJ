import random
from Classes.CarClass import Car

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

        self._original_board = [row[:] for row in self._board]


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
                return False
        elif direction == -1:
            target_row = base[0] - rotation[0]
            target_col = base[1] - rotation[1]
        else:
            print("Invalid move!")
            return False
        
        if self._board[target_row][target_col] != 0 or target_col < 0 or target_row < 0:
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

    def show_board(self):
        """
        An alternative and more simplified board that relies on print-statements.
        """
        size = int(self.game_file.board_size)
        exit_row = {6: 2, 9: 4, 12: 5}[size]

        def park_car(column):
            if column != 0:
                car = self._dictionary_of_cars[column].get_name_colored()
                print(f"{car}|", end="")
            else:
                print("    |", end="")

        def draw_line(size):
            print("\n+" + "====+" * size)
        
        draw_line(size)

        for i, row in enumerate(self._board):
            print("|", end="")
            for column in row:
                park_car(column)

            if i == exit_row or i == exit_row - 1:
                draw_line(size + 1)
            else:
                draw_line(size)


    def is_won(self):
        if (self._dictionary_of_cars['X'].get_base()[1]) >= ((len(self.get_board()[0])) - 2):
            return True
        return False


    def get_board(self):
        """
        Returns the current state of the game board.
        """
        return self._board
    

    def is_legal_move(self, letter, direction) -> bool:
        """
        ik gebruik deze in algoritme make_random_legal_move , voor nu ff zo
        is gwn copy paste uit move car

        geef naam en direction en krijg True/False terug

        """
        car = self._dictionary_of_cars[letter]
        base = car.get_base()
        rotation = car.get_rotation()
        length = car.get_length()

        if direction == 1:
            target_row = base[0] + (rotation[0] * length)
            target_col = base[1] + (rotation[1] * length)
        elif direction == -1:
            target_row = base[0] - rotation[0]
            target_col = base[1] - rotation[1]
        else:
            return False

        if (target_row >= len(self._board) or target_col >= len(self._board) or
                target_row < 0 or target_col < 0 or
                self._board[target_row][target_col] != 0):
            return False

        return True


    def get_all_legal_moves(self):

        moves = []

        for name in self.game_file.get_car_names():
            for direction in [1, -1]:
                if self.is_legal_move(name, direction):
                    moves.append((name, direction))
        return moves
    

    def get_board_as_hash(self, board):
        """
        Elk bord kan je zien als string ja.
        Maak van die string een hash
        Dit is een int uniek voor deze string
        
        """
        board_string = ''
        for row in board:
            board_string += ''.join(str(row)) + ';'
        return hash(board_string)

    def reset_board(self):
        self.set_board(self._original_board)

    def set_board(self, new_board):
        """
        Sets the board to the given state and updates the positions of the cars.
        """
        self._board = [row[:] for row in new_board]  # je kan niet gwn = doen want list list
        self._update_car_bases()


    def _update_car_bases(self):
        """
        Updates the base of the cars in _dictionary_of_cars based on the current board state.
        """
        # Set car base to null null
        for car in self._dictionary_of_cars.values():
            car.reset_base()

        # Iterate over the board and update car base
        # The base of the car is always the first it finds
        for row_idx, row in enumerate(self._board):
            for col_idx, cell in enumerate(row):
                if cell != 0: 
                    car = self._dictionary_of_cars[cell]
                    if not car.is_base_set():
                        car.set_base(row_idx, col_idx) # Update the car's base


    def generate_all_possible_succesor_boards(self):
        """
        Take all legal moves, execute them, and save the board along with the move made.
        Return a list of tuples, (successor board, and the move that led to it)
        """
        successor_states = []
        original_board = [row[:] for row in self._board]  # Make a copy, cant do just = 

        all_legal_moves = self.get_all_legal_moves()

        for move in all_legal_moves:
            self.move_car(move[0], move[1])

            # Add the board and move to list
            new_state_board = [row[:] for row in self._board]
            successor_states.append((new_state_board, move))
            
            # Reset board to original
            self.set_board(original_board)

        return successor_states

    def red_at_exit(self, board):
        exit_row = {6: 2, 9: 4, 12: 5}[len(board)]
        return board[exit_row][-1] == 'X'

    def red_score(self, board) -> int:
        exit_row = {6: 2, 9: 4, 12: 5}[len(board)]
        return len(board) - board[exit_row].index('X')

    def cars_blocking_red(self, board) -> int:
        exit_row = {6: 2, 9: 4, 12: 5}[len(board)]
        red_index = board[exit_row].index('X')

        score = 0
        for cell in board[red_index:]:
            if cell != 'X' and cell != 0:
                score += 1
        return score

    def score(self, board) -> int:
        return self.red_score(board) + self.cars_blocking_red(board)