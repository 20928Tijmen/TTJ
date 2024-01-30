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

        self.total_boards_per_depth = {0: 1}
        self.unique_boards_per_depth = {0: 1}


    def run(self) -> list:
        self.queue = deque()
        self.visited = set()

        self.total_boards_per_depth = {0: 1}
        self.unique_boards_per_depth = {0: 1}

        self.queue.append((self.game.get_board(), [], 0))
        self.visited.add(self.game.get_board_as_hash(self.game.get_board()))


        while self.queue:
            current_board, path, depth = self.queue.popleft()
            self.game.set_board(current_board)

            for successor_board, move in self.game.generate_all_possible_successor_boards():

                self.total_boards_per_depth[depth + 1] = self.total_boards_per_depth.get(depth + 1, 0) + 1

                board_hash = self.game.get_board_as_hash(successor_board)
                               
                if board_hash not in self.visited:

                    self.unique_boards_per_depth[depth + 1] = self.unique_boards_per_depth.get(depth + 1, 0) + 1

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        self.game.set_board(successor_board)
                        return path, len(self.visited)
                    
                    self.visited.add(board_hash)

                    new_path = path + [move]

                    self.queue.append((successor_board, new_path, depth + 1))

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

    def layered_depth_data_csv_output(self):
        """
        Exports the depth data to a CSV file.
        """
        results_dir = 'Layered_data_BFS'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        file_name = 'Layered_Data_BFS_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'
        file_path = os.path.join(results_dir, file_name)

        if os.path.exists(file_path):
            print(f"{file_name} already exists. CSV not created.")
            return 

        with open(file_path, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['depth', 'total_boards', 'unique_boards'])
            for depth in range(len(self.total_boards_per_depth)):
                total_boards = self.total_boards_per_depth.get(depth, 0)
                unique_boards = self.unique_boards_per_depth.get(depth, 0)
                writer.writerow([depth, total_boards, unique_boards])


    def summed_depth_data_csv_output(self):
        """
        Exports the summed depth data to a CSV file.
        """
        results_dir = 'Summed_Data_BFS'
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        file_name = 'Summed_Data_BFS_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'
        file_path = os.path.join(results_dir, file_name)

        if os.path.exists(file_path):
            print(f"{file_name} already exists. CSV not created.")
            return 

        summed_total_boards = 0
        summed_unique_boards = 0

        with open(file_path, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['depth', 'summed_total_boards', 'summed_unique_boards'])
            for depth in range(len(self.total_boards_per_depth)):
                total_boards = self.total_boards_per_depth.get(depth, 0)
                unique_boards = self.unique_boards_per_depth.get(depth, 0)

                summed_total_boards += total_boards
                summed_unique_boards += unique_boards

                writer.writerow([depth, summed_total_boards, summed_unique_boards])
