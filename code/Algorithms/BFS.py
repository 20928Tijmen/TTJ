<<<<<<< HEAD
from collections import deque
import csv, os

class BFS:


    def __init__(self, game):
        self.game = game
        self._path_found = []


    def run(self):

        self.queue = deque()
        self.visited = set()

        self.queue.append((self.game.get_board(), []))
        self.visited.add(self.game.get_board_as_hash(self.game.get_board()))

        while self.queue:
            current_board, path = self.queue.popleft()
            self.game.set_board(current_board)

            for successor_board, move in self.game.generate_all_possible_successor_boards():

                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in self.visited:

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        self.game.set_board(successor_board)
                        return path, len(self.visited)
                    
                    self.visited.add(board_hash)

                    new_path = path + [move]

                    self.queue.append((successor_board, new_path))

        return None  # No solution found


    def csv_output(self):
        """
        Exports the compressed BFS move history to a CSV file.

        Zie mapje results.

        """
        results_dir = 'Results_BFS'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        file_name = 'output_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'

        file_path = os.path.join(results_dir, file_name)

        if os.path.exists(file_path):
            print(f"{file_name} already exists. csv not created.")
            return 

        compressed_history = [self._path_found[0]]

        for move in self._path_found[1:]:
            last_move = compressed_history[-1]
            if move[0] == last_move[0]:
                new_move = (move[0], last_move[1] + move[1])
                compressed_history[-1] = new_move
            else:
                compressed_history.append(move)

        with open(file_path, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['car', 'move'])
            for move in compressed_history:
                writer.writerow(move)
=======
from collections import deque
import csv, os

class BFS:
    """
    Implementation of a breadth first searching algorithm based on our version of rushhour
    Goos threw every possible board, starting board -> all their childeren -> all THEIR childer etc.

    input:
    game: GameBoard = A gameboard for the algorithm to "solve"

    methods:
    run = the actual search algoritm. returns found path + stores it in path_found
    csv_output = turns the found path into a csv file where repeated moves are compressed
    
    """


    def __init__(self, game) -> None:
        self.game = game
        self._path_found = []


    def run(self) -> list:
        self.queue = deque()
        self.visited = set()

        self.queue.append((self.game.get_board(), []))
        self.visited.add(self.game.get_board_as_hash(self.game.get_board()))

        while self.queue:
            current_board, path = self.queue.popleft()
            self.game.set_board(current_board)

            for successor_board, move in self.game.generate_all_possible_successor_boards():

                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in self.visited:

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        self.game.set_board(successor_board)
                        return path, len(self.visited)
                    
                    self.visited.add(board_hash)

                    new_path = path + [move]

                    self.queue.append((successor_board, new_path))

        return None  # No solution found


    def csv_output(self):
        """
        Exports the compressed BFS move history to a CSV file.

        Zie mapje results.

        """
        results_dir = 'Results_BFS'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        file_name = 'BFS_output_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'

        file_path = os.path.join(results_dir, file_name)

        if os.path.exists(file_path):
            print(f"{file_name} already exists. csv not created.")
            return 

        compressed_history = [self._path_found[0]]

        for move in self._path_found[1:]:
            last_move = compressed_history[-1]
            if move[0] == last_move[0]:
                new_move = (move[0], last_move[1] + move[1])
                compressed_history[-1] = new_move
            else:
                compressed_history.append(move)

        with open(file_path, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['car', 'move'])
            for move in compressed_history:
                writer.writerow(move)
>>>>>>> f137e6ca50ca091c74b0b76170d38e19afd71390
