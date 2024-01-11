#from GameBoardClass import GameBoard
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
    - path_list: list[string] = voor elke file in de aangewezen folder -> relatieve pad + filenaam
    
    '''

    file_paths = []

    for file in os.listdir(path):
        single_file_path = os.path.join(path, file)
        file_paths.append(single_file_path)
    
    return file_paths
    
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

    # lijst van paths naar alle bord opstellingen
    paths_all = load_board_opstellingen('RushHourJoost/data') # Hangt af hoe de directory is opgebouwd natuurlijk

    # prompt for size board
    board_size = input("What board size would like like?\nOptions: 6, 9, 12\nInput here: ")

    # get a list of board with given size, and a list with their numbers to pick from
    path_options, board_options = get_paths_of_size(paths_all, board_size)

    # make it look pretty when printed
    formatted_board_options = ", ".join(board_options)

    # prompt for which of the boards the player wants to use
    game_number = input(f"Boards with size {board_size}\nOptions: {formatted_board_options}\nInput here: ")

    # get the desired path from the options
    path_FINAL = get_path_of_number(game_number, path_options)

    return path_FINAL

def pick_board_random() -> str:
    '''
    spreekt voorzich denk ik
    '''

    paths_all = load_board_opstellingen('RushHourJoost/data') # Hangt af hoe de directory is opgebouwd natuurlijk

    return random.choice(paths_all)


if __name__ == '__main__':

    if input("random?  yes/no  : ") == 'yes':
        # voor random bord
        file_path = pick_board_random()
    else:
        # for human player, pick a board with prompted questions
        file_path = pick_board_manualy()







'''
    game = GameBoard()
    game.add_cars()

    board = game.get_board()
    fancy_board = game.get_board_for_player()
    print(fancy_board)    

    while True:
        letter = input("give car letter:  ")
        direction = int(input("give direction. 1 or -1:  " ))

        game.move_car(letter, direction)

        print(game.get_board_for_player())
'''