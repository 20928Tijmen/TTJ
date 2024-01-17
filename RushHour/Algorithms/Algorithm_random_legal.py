import random

def make_random_legal_move(game) -> (str, int):
    """
    make a random legal move by first making a random move, but remaking if its an illegal move


    pre:    game: GameBoard = zelfde gebruik als random + je wilt is_legal_move() bereiken dus vandaar hele game 

    post:   random_car: string = a randomly picked name from the list of car names
            random_direction: int = pakt random 1 of -1
    
    test: the average amount of moves needed for 100 games was 76832.84 moves, and 76832.84 game loops
    """

    
    # choose random car from names in game file
    random_car = random.choice(game.game_file.get_car_names())
    # choose random move
    random_direction = random.choice([1, -1])

    while game.is_legal_move(random_car, random_direction) == False:

        random_car, random_direction = make_random_legal_move(game)
    
    return random_car, random_direction


