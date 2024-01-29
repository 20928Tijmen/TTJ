
class Node:
    '''
    voor A* heeft elk bord:
    
    - een score adhv heuristieken 
    - een diepte / hoeveel moves naar deze opstelling
    - een bord opstelling
    - een pad ernaartoe, de moves in volgorde
    
    
    '''
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
