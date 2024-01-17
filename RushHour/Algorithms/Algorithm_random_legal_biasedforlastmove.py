import random

def make_random_legal_move_biased_to_repeat_last_move(game, history) -> (str, int):
    """
    make a random legal move by first making a random move, but remaking if its an illegal move

    pre:    game: GameBoard = zelfde gebruik als random + je wilt is_legal_move() bereiken dus vandaar hele game 

    post:   random_car: string = a randomly picked name from the list of car names
            random_direction: int = pakt random 1 of -1
    
    test: the average amount of moves needed for 100 games was 21160.38 moves, and 21160.38 game loops
    """
    
    previous_move = history.previous_move

    if previous_move and game.is_legal_move(previous_move[0], previous_move[1]):

        return history.previous_move
    
    # choose random car from names in game file
    random_car = random.choice(game.game_file.get_car_names())
    # choose random move
    random_direction = random.choice([1, -1])

    while game.is_legal_move(random_car, random_direction) == False:

        random_car, random_direction = make_random_legal_move_biased_to_repeat_last_move(game)
    
    return random_car, random_direction