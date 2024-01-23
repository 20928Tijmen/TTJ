from collections import deque
import csv, os, heapq

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

            
            for successor_board, move in self.game.generate_all_possible_succesor_boards():

                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in self.visited:

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        return path, len(self.visited)
                    
                    self.visited.add(board_hash)

                    new_path = path + [move]

                    self.queue.append((successor_board, new_path))

        return None  # No solution found


    def run_w_repeat_heuristik(self):
        """
        somehow worse..
        """
        self.queue = deque()
        self.visited = set()

        self.queue.append((self.game.get_board(), []))
        self.visited.add(self.game.get_board_as_hash(self.game.get_board()))

        while self.queue:
            current_board, path = self.queue.popleft()
            self.game.set_board(current_board)

            if self.game.red_at_exit(current_board): 
                self._path_found = path
                return path, len(self.visited)

            last_move = path[-1] if path else None

            for successor_board, move in self.game.generate_all_possible_succesor_boards():
                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in self.visited:

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        return path, len(self.visited)
                    
                    self.visited.add(board_hash)

                    new_path = path + [move]

                    # If the move is a repeated move, prioritize it
                    if move == last_move:
                        self.queue.appendleft((successor_board, new_path))  # Append to left
                    else:
                        self.queue.append((successor_board, new_path))  # Append to right

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

    

    def Astar(self):

        depth = 0
        priority_q = list(tuple())
        visited = set()
        root_node = Node(self.game.score(self.game.get_board()), depth, self.game.get_board(), [])
        heapq.heappush(priority_q, root_node)

        while priority_q:
            node = heapq.heappop(priority_q)
            score, depth, current_board, path = node.extract()

            self.game.set_board(current_board)

            
            for successor_board, move in self.game.generate_all_possible_succesor_boards():

                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in visited:

                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        return path, len(visited)
                    
                    visited.add(board_hash)

                    new_path = path + [move]

                    node = Node(self.game.score(successor_board), depth + 1, successor_board, new_path)

                    heapq.heappush(priority_q, node)

        return None  # No solution found


class Node:
    def __init__(self, score, depth, current_board, path):

        self.score = score
        self.depth = depth
        self.current_board = current_board
        self.path = path

    def __le__(self, other):
        return self.score <= other.score

    def __lt__(self, other):
        return self.score < other.score

    def extract(self):
        return self.score, self.depth, self.current_board, self.path