from Algorithms import BFS, RandomMove, RandomLegalMove, RandomLegalRepeatMove
from Classes import GameBoard, GameFile, History

# pip3 install matplotlib numpy
    
import numpy as np
import matplotlib.pyplot as plt

import os, random


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
    board_size = input("What board size would you like?\nOptions: 6, 9, 12\nInput here: ")
    path_options, board_options = get_paths_of_size(paths_all, board_size)
    game_number = input(f"Boards with size {board_size}\nOptions: {', '.join(board_options)}\nInput here: ")
    return get_path_of_number(game_number, path_options)


def pick_board_random() -> str:
    '''
    spreekt voorzich denk ik
    '''
    return random.choice(load_board_opstellingen('data'))


def visual():
    """
    Main function to run the Rush Hour game.
    """
    # Create an instance of the History class
    history = History()

    if input("Random board? yes/no : ") == 'yes':
        file_path = pick_board_random()
    else:
        available_board_dictionary = available_boards()
        board_pick = str
        while board_pick not in available_board_dictionary:
            board_pick = str(input("Which board will you pick? "))

        file_path = available_board_dictionary[board_pick]  

    algorithms = available_algorithms()
    select_algorithm = str
    while select_algorithm not in algorithms:
        select_algorithm = input("Choose an algorithm: ").lower()

        selected_algorithm = algorithms[select_algorithm]
    
    
    game_file = GameFile(file_path)
    game = GameBoard(game_file)

    while True:


        # This script plays when the game is won
        if (game.is_won()):
            print("Congratulations, you found your way out!")
            print('Total moves:',history.get_counter())
            break

        # ask user for input
        random_move_algorithm = selected_algorithm(game, history, game_file)
        random_car, random_direction = random_move_algorithm.make_move()
        
        if game.move_car(random_car, random_direction) is not False:
            history.add_move(random_car, random_direction)
            history.add_board(game.get_board())

        game.show_board()
        print('Move count:',history.get_counter())
        print(history.get_move_history())
        continue
        
        # give user the possibility to go back
        if letter == "BACK":
            if history.get_counter() < 1:
                print("Must have a history of moves")
                continue

            # make the move back
            game.make_move_back(history)

            # update the history list
            history.go_back()

def available_boards():
    print("\nAvailable boards:\n")
    # Hier staan alle borden.
    boards_dictionary = {
        '1': "data/Rushhour6x6_1.csv",
        '2': "data/Rushhour6x6_2.csv",
        '3': "data/Rushhour6x6_3.csv",
        '4': "data/Rushhour9x9_4.csv",
        '5': "data/Rushhour9x9_5.csv",
        '6': "data/Rushhour9x9_6.csv",
        '7': "data/Rushhour12x12_7.csv",
    }
    
    board_sizes = ['6x6', '6x6', '6x6', '9x9', '9x9', '9x9', '12x12']

    for i in range(len(boards_dictionary)):
        print(f'{i + 1}: {board_sizes[i]}\n')

    return boards_dictionary


def available_algorithms():
    print("\nAvailable algorithms:\n")
    # Hierin kun je de beschikbare algoritmes plaatsen!
    algorithms_dictionary = {
        "1": RandomLegalMove,
        "2": RandomLegalRepeatMove,
        "3": RandomMove,
        "4": BFS,
    }

    algorithm_names = ['RandomLegalMove', 'RandomLegalRepeatMove', 'RandomMove', 'BFS']

    for i in range (len(algorithms_dictionary)):
        print(f'{i + 1}: {algorithm_names[i]}\n')

    return algorithms_dictionary


def print_in_barchart(data_dict):
    X_data = list(data_dict.keys())
    Y_data = list(data_dict.values())
    amount_of_times_run = 10000

    plt.bar(X_data, Y_data)
    plt.title(f'Ran algorithms {amount_of_times_run} times on 6x6_1')
    plt.xlabel('Algorithms')
    plt.ylabel('Average amount of moves made')

    # Save the plot to a file
    picture = plt.savefig(str(input("Picture name? ")))

    # Display a message to the user
    print(f"The result is saved as {picture}. Please check the files!")

def save_data():
    None

# list of algorithms used
algorithms_used_and_their_average_moves = {}


def experiment():

    # needed moves word hierin opgeslagen na solve
    total_moves = []

    # illegal moves worden niet bijgehouden, dus tel OOK hoevaak de game loop gerund word
    total_loops = []

    number_of_games = int(input("\nHow many games do you want to run for this experiment? "))
    
    available_board_dictionary = available_boards()
    board_pick = str
    while board_pick not in available_board_dictionary:
        board_pick = str(input("Which board will you pick? "))

    algorithms = available_algorithms()
    select_algorithm = str
    while select_algorithm not in algorithms:
        select_algorithm = input("Choose an algorithm: ").lower()

    selected_algorithm = algorithms[select_algorithm]
        
    for i in range(number_of_games):

        history = History()

        file_path = available_board_dictionary[board_pick]

        game_file = GameFile(file_path)
        game = GameBoard(game_file)

        loop_counter = 0

        while True:
            
            if game.is_won():
                print(f"game {i + 1} was solved in {history.get_counter()} moves, and {loop_counter} game loops")
                total_moves.append(history.get_counter())
                total_loops.append(loop_counter)
                break


            random_move_algorithm = selected_algorithm(game, history, game_file)
            random_car, random_direction = random_move_algorithm.make_move()

            if game.move_car(random_car, random_direction):
                history.add_move(random_car, random_direction)
                history.add_board(game.get_board())
            
            loop_counter += 1

    average_moves = (sum(total_moves) / len(total_moves))
    average_loops = (sum(total_loops) / len(total_loops))

    print(history.get_board_history())
    
    # Add to list of algorithms used and their average moves made
    algorithms_used_and_their_average_moves[select_algorithm] = average_moves

    print(f"\nThe average amount of moves needed for {number_of_games} games was {average_moves} moves, and {average_loops} game loops")


def breadth_first_search1():

    available_board_dictionary = available_boards()
    board_pick = str
    while board_pick not in available_board_dictionary:
        board_pick = str(input("Which board will you pick? "))    

    file_path = available_board_dictionary[board_pick]

    game_file = GameFile(file_path)
    game = GameBoard(game_file)
    
    game.show_board()

    bfs = BFS(game).run()
    visual = GameBoard(game_file)

    for move in bfs:
        print(f"Move car {move[0]} in direction {move[1]}")
        visual.move_car(move[0], move[1])
        visual.show_board()


def main():

    while True:

        mode = str
        while mode not in ['v', 'e', 'b']:
            mode = input("\nDo you want to run the game in the Visual mode, or in the Experiment mode, or in BFS? (v/e/b) ").lower()
    
        if mode == 'v':
            visual()
        elif mode == 'e':
            experiment()
        elif mode == 'b':
            breadth_first_search1()

        continu = str
        while continu not in ['q', 'c']:
            continu = input("\nDo you want to continue, or quit? (c/q) ")

        if continu == 'q':
            # prints into a barchart
            print_in_barchart(algorithms_used_and_their_average_moves)
            break
        elif continu == 'c':
            continue


import time 

def Joosts_test_paradijs():
    file_path = 'data/Rushhour9x9_4.csv'
    game_file = GameFile(file_path)

    game = GameBoard(game_file)
    bfs = BFS(game)
    
    results = bfs.run()
    print(len(results[0]), results[1])



if __name__ == '__main__':
    
    # Joosts_test_paradijs()
    main()


# file met allemaal verschillende algoritmes.
# radio russia repository
# madplotlib
# codebase belangirjk!!
# voor presentatie alleen kijken naar algoritmes 
# algoritmes als classes!
    

#lecture maandag week 3:
    # zet de algoritmes tegenover elkaar
        # veel resultaten!
    #(unit)tests
    # kloppen all tussenstappen? springt een auto over een auto heen?


# Reproducibility!!!!! Deze is belangrijk:
    # Deel de code
    # Deel de input
    # Documenteer hoe de code is ....?
    #
    #

#Tips:
# Schrijf scripts voor de experimenten
# Liever te veel data, dan te weinig
# Gebruik een "seed" bij random algoritmes.
# Schrijf scripts voor het visualiseren van resultaten
# requirements.txt!!!!!!!!!!!!!!! belangrijk voor matplotlib, Thijs gebruikt een oudere versie, dus anderen moeten testen of het werkt met hun versie.
# Schijf scripts!!!
    

# algoritmes vegelijken:
    # Tijd en ruimte

    # Tijd: dezelfde computer, rapporteer specs: Proceser, deel de code, gebruik geen profiler

    # median is belangrijker dan mean! Dus boxplot is wel handig denk ik

# from statistics import variance, stdev
    

# kijk uit met claims
# Buggy implementaties...?
# under promise, over deliver
# geef een oplossing voor de case
    
# one factor at a time
# grid search : paken twee parameters en .....
    

#constructieve algoritme maken
    

    #introductie:wij zijn ttj,oftewel tijmen, thijs, joost. Rushhour is een schuifpuzzel die in de jaren 70 bedacht is door Nobuyuki Yoshigahara.
    # case uitleggen 
    # statespase uitleggen: twee tot de macht n, waar n bordlengte keer bordlengte is
    # nooit een auto ervoor horizontaal, auto is altijd met XX en rood aangegeven
    #  uitleggen dat we in stappen van 1 en winst is dat de auto daar rechts staat