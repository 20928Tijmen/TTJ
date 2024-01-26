from Classes import Node
import heapq


class Astar:
    """
    Implementation of a A* searching algorithm based on our version of rushhour
    Works similar to BFS, but the difference lies in the order of exploration of child nodes

    The order in which child nodes are explored is based on each board heuristical score
    lower score = higer priority

    score is calculated based on depth, red car distance, blocking vehicles
    depth = the amount of moves needed to get to this board
    red car score = how many cell is the red car away from the exit
    blocking vehicles = how many cars are in the way of red and the exit

    input:
    game: GameBoard = A gameboard for the algorithm to "solve"

    methods:
    run = the actual search algoritm. returns found path + stores it in path_found

    """


    def __init__(self, game):
        self.game = game
        self._path_found = []

    def run(self):
        depth = 0
        priority_q = []
        visited = set()
        root_node = Node(self.game.score(self.game.get_board()), depth, self.game.get_board(), [])
        heapq.heappush(priority_q, root_node)

        while priority_q:
            node = heapq.heappop(priority_q)
            score, depth, current_board, path = node.extract()
            self.game.set_board(current_board)

            for successor_board, move in self.game.generate_all_possible_successor_boards():
                board_hash = self.game.get_board_as_hash(successor_board)

                if board_hash not in visited:
                    if self.game.red_at_exit(successor_board): 
                        self._path_found = path + [move]
                        self.game.set_board(successor_board)
                        return path, len(visited)
                    
                    visited.add(board_hash)
                    new_path = path + [move]
                    node = Node(self.game.score(successor_board) + depth, depth + 1, successor_board, new_path)
                    heapq.heappush(priority_q, node)

        return None  # No solution found


   