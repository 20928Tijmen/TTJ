import random


def make_random_move(game_file) -> (str, int):
    """
    make a random move

    pre:    game_file: GameFile = game file van current game, to extract what car names are used

    post:   random_car: string = a randomly picked name from the list of car names
            random_direction: int = pakt random 1 of -1

    test: the average amount of moves needed for 10 games was 95695.6 moves, and 374166.4 game loops
    """

    # choose random car from names in game file
    random_car = random.choice(game_file.get_car_names())
    # choose random move
    random_direction = random.choice([1, -1])
    
    return random_car, random_direction