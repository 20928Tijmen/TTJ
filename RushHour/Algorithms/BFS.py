from collections import deque

class BFS:
    def __init__(self, game):
        self.game = game
        self.queue = deque([([row[:] for row in game.get_board()], [])]) 
        self.visited = set([game.get_board_as_hash()])

    def run(self):
        while self.queue:
            current_board, path = self.queue.popleft()
            self.game.set_board(current_board)

            if self.game.is_won(): 
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