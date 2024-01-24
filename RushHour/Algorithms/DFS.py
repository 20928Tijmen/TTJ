from collections import deque
import csv, os, heapq

class DFS:
    def __init__(self, game):
        self.game = game
        self._path_found = []

    def run(self):
        self.queue = deque()
        self.visited = set()




    def csv_output(self):
        """
        Exports the compressed BFS move history to a CSV file.
        Zie mapje results.
        """
        results_DFS_dir = 'Results'
        if not os.path.exists(results_DFS_dir):
            os.makedirs(results_DFS_dir)

        file_name = 'output_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'

        file_path = os.path.join(results_DFS_dir, file_name)

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