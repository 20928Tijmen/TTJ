import random

class RandomLegalMove:
    """
    make a random legal move by first making a random move, but remaking if its an illegal move

    pre:    game: GameBoard = zelfde gebruik als random + je wilt is_legal_move() bereiken dus vandaar hele game 

    post:   random_car: string = a randomly picked name from the list of car names
            random_direction: int = pakt random 1 of -1
    
    """
    
    def __init__(self, game):
        self.game = game

    def make_move(self):
        random_car = random.choice(self.game.game_file.get_car_names())
        random_direction = random.choice([1, -1])

        while self.game.is_legal_move(random_car, random_direction) == False:
            random_car, random_direction = self.make_move()
        
        return random_car, random_direction
