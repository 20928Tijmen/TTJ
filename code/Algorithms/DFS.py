from collections import deque
import csv, os, heapq




class DFS:
    """
    pre-order depth first search algorithm
    """
    def __init__(self, game):

        # Constructor: Initialize DFS with the game instance
        self.game = game
        self._path_found = []  # Path found during DFS traversal

    def run(self):
        # Initialize a stack to use as a stack for DFS
        self.stack = []
        # Set to keep track of visited states to avoid revisiting
        self.visited = set()

        # Add the initial state of the game to the stack with an empty path
        self.stack.append((self.game.get_board(), []))
        # Mark the initial state as visited
        self.visited.add(self.game.get_board_as_hash(self.game.get_board()))

        # Main DFS loop
        while self.stack:
            # Get the current state and the path taken so far
            current_board, path = self.stack.pop()
            # Update the game board to the current state
            self.game.set_board(current_board)

            # Generate all possible successor boards and moves for the current state
            for successor_board, move in self.game.generate_all_possible_successor_boards():

                # Generate a hash for the successor board to check if it's visited
                board_hash = self.game.get_board_as_hash(successor_board)

                # Check if the successor board is not visited
                if board_hash not in self.visited:
                    # Check if the red car is at the exit position
                    if self.game.red_at_exit(successor_board):
                        # If the red car is at the exit, a solution is found
                        self._path_found = path + [move]
                        self.game.set_board(successor_board)
                        return path, len(self.visited)
                    
                    # Mark the successor board as visited
                    self.visited.add(board_hash)
                    # Update the path with the current move
                    new_path = path + [move]
                    # Add the successor board and its path to the stack for further exploration
                    self.stack.append((successor_board, new_path))

        # If the stack becomes empty and no solution is found returns None
        return None  


    def csv_output(self):
        """
        Exports the compressed DFS move history to a CSV file.
        Zie mapje results.
        """
        data_dir = 'data'
        results_subdir = 'results_DFS'
        results_dir = os.path.join(data_dir, results_subdir)

        if not os.path.exists(results_dir):
            os.makedirs(results_dir)

        file_name = 'DFS_output_' + str(self.game.game_file.board_size) + '_' + str(self.game.game_file.number) + '.csv'

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