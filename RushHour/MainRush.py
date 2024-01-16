
from GameBoardClass import GameBoard
from GameFileClass import GameFile
from History import History
from Algorithms.Algorithm_random import *
import os
import random

# import os voor uitlezen van een folder in load_board_opstellingen()
# import random voor pick_board_random()

def load_board_opstellingen(path: str) -> list[str]:
    '''
    Zet alle gegeven bord csv's in een folder
    geef van deze folder de path als input
    krijg een mooie lijst me paths naar elke bord file terug

    input: 
    - path: string = het relative path voor de folder waarin alle csv files voor de borden in staan
    
    output:  
    - return: list[string] = voor elke file in de aangewezen folder -> relatieve pad + filenaam
    
    '''

    return [os.path.join(path, file) for file in os.listdir(path)]
    

def get_paths_of_size(file_paths: list[str], size: str):
    '''
    geef alle paths en gewenste size 
    je krijgt een lijst met paths van die size , 
    en een lijst met de nummers van die borden
    !! PATH FORMAT MOET EINDIGEN OP *6x6_1.csv of *12x12_1.csv WEGENS INDEXING !!

    input:
    - file_paths: list[str] = de paths naar alle borden 
    - size: str = de player input word als string gelezen

    output:
    - paths: list[str] = lijst van filepaths met de gevraagde size
    - options: list[str] = lijst met de board nummers, want zijn meerdere van elke size
    
    '''

    paths = []
    options = []

    for path in file_paths:
        if path[-7] == size[0] or path[-8] == size[0]: 
            paths.append(path)
            options.append(path[-5])

    options = sorted(options)

    return paths, options


def get_path_of_number(game_number: str, path_options: list[str]) -> str:
    '''
    bij input '3' krijg je het het eerste bord eindigend op 3.csv terug
    '''
    for path in path_options:
        if path[-5] == game_number: 
            return path
    

def pick_board_manualy() -> str:
    '''
    deze functie start een gesprek met de speler in de terminal
    zo kies je een spel uit
    '''
    paths_all = load_board_opstellingen('data')
    board_size = input("What board size would like like?\nOptions: 6, 9, 12\nInput here: ")
    path_options, board_options = get_paths_of_size(paths_all, board_size)
    game_number = input(f"Boards with size {board_size}\nOptions: {', '.join(board_options)}\nInput here: ")
    return get_path_of_number(game_number, path_options)


def pick_board_random() -> str:
    '''
    spreekt voorzich denk ik
    '''
    return random.choice(load_board_opstellingen('data'))


def main():
    """
    Main function to run the Rush Hour game.
    """
    # Create an instance of the History class
    history = History()

    file_path = pick_board_random() if input("random? yes/no : ") == 'yes' else pick_board_manualy()
    game_file = GameFile(file_path)
    game = GameBoard(game_file)

    gameplay = 'Game'

    while gameplay not in ['Automatic', 'Manual', 'm', 'a', 'M', 'A']:
        gameplay = input("Automatic or Manual? ")

    if gameplay == "Automatic" or gameplay == "A" or gameplay == "a":
        algo = int(input("Which algorithm? 1, or 2? "))
        if algo == 1:
            algorithm = None
        elif algo == 2:
            algorithm = None

    print(game.get_board_for_player())

    while True:
    
        # This script plays when the game is won
        if (game.is_won()):
            print("Congratulations, you found your way out!")
            print('Total moves:',history.get_counter())
            break

        # ask user for input
        if gameplay == 'Automatic' or gameplay == 'a' or gameplay == 'A':
            letter = algorithm.random_car()
        elif gameplay == 'Manual' or gameplay == 'm' or gameplay == 'M':
            letter = input("give car letter: ").upper()

            # give user the possibility to go back
            if letter == "BACK":
                if history.get_counter() < 1:
                    print("Must have a history of moves")
                    continue

                # make the move back
                game.make_move_back(history)

                # update the history list
                history.go_back()

                # print for users
                print(game.get_board_for_player())
                print('Move count:',history.get_counter())
                print(history.get_move_history())
                continue

            direction = input("give direction: -1 or 1").upper()

            # Make move and add move and board to history
            if game.move_car(letter, direction) is not False:
                history.add_move(letter, direction)
                history.add_board(game.get_board())

            # print for users
            print(game.get_board_for_player())
            print('Move count:',history.get_counter())
            print(history.get_move_history())


def test_main_dinges():

    # needed moves word hierin opgeslagen na solve
    total_moves = []

    # illegal moves worden niet bijgehouden, dus tel OOK hoevaak de game loop gerund word
    total_loops = []

    # solve gegeven aantal keer de 12x12 game op
    # geeft score door aan total moves en loops
    number_of_games = 10
    for i in range(number_of_games):

        history = History()

        file_path = 'data/Rushhour12x12_7.csv'

        game_file = GameFile(file_path)
        game = GameBoard(game_file)

        loop_counter = 0

        while True:
            
            if game.is_won():
                print(f"game {i + 1} was solved in {history.get_counter()} moves, and {loop_counter} game loops")
                total_moves.append(history.get_counter())
                total_loops.append(loop_counter)
                break

            #   Kies je algoritme om te testen, maar 1 per keer natuurlijk
            #   maak de rest comments, (NIET OM INPUT GAAN VRAGEN)
            #
            random_car, random_direction = make_random_legal_move_biased_to_repeat_last_move(game, history)
            #random_car, random_direction = make_random_legal_move(game)
            #random_car, random_direction = make_random_move(game_file)

            if game.move_car(random_car, random_direction):
                history.add_move(random_car, random_direction)
                history.add_board(game.get_board())
            
            loop_counter += 1

    average_moves = (sum(total_moves) / len(total_moves))
    average_loops = (sum(total_loops) / len(total_loops))


    print(f"the average amount of moves needed for {number_of_games} games was {average_moves} moves, and {average_loops} game loops")

if __name__ == '__main__':

    test_main_dinges()
    #main()