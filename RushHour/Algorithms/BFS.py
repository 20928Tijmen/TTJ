from collections import deque
import csv, os

class BFS:
    def __init__(self, game):
        self.game = game
        self.queue = deque([([row[:] for row in game.get_board()], [])]) 
        self.visited = set([game.get_board_as_hash()])

        self._path_found = []

    def run(self):
        while self.queue:
            current_board, path = self.queue.popleft()
            self.game.set_board(current_board)

            if self.game.is_won(): 
                self._path_found = path
                return path 

            
            for successor_board, move in self.game.generate_all_possible_succesor_boards():
                self.game.set_board(successor_board)
                board_hash = self.game.get_board_as_hash()

                if board_hash not in self.visited:
                    self.visited.add(board_hash)

                    new_board = [row[:] for row in successor_board]

                    new_path = path + [move]

                    self.queue.append((new_board, new_path))

        return None  # No solution found


    def csv_output(self):
        """
        Exports the compressed BFS move history to a CSV file.

        Zie mapje results.

        """
        results_dir = 'Results'
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