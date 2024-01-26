from Algorithms import DFS, BFS, Astar, RandomMove, RandomLegalMove, RandomLegalRepeatMove
from Classes import GameBoard, GameFile, History

# pip3 install matplotlib numpy
    
import numpy as np
import matplotlib.pyplot as plt

import os, random

import pygame
import time 
import timeit

import csv


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
    }

    algorithm_names = ['RandomLegalMove', 'RandomLegalRepeatMove', 'RandomMove']

    for i in range (len(algorithms_dictionary)):
        print(f'{i + 1}: {algorithm_names[i]}\n')

    return algorithms_dictionary

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
    
    # Initializes the 'pygame'-part of the code.
    pygame.init()

    # This sets up the display of the pygame.
    rows = len(game._board)
    cols = len(game._board[0])
    screen = pygame.display.set_mode((cols * 50, rows * 50))
    pygame.display.set_caption("Rush-Hour Board")

    clock = pygame.time.Clock() 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # This script plays when the game is won
        if game.is_won():
            print("Congratulations, you found your way out!")
            print('Total moves:', history.get_counter())
            running = False 


        random_move_algorithm = selected_algorithm(game, history, game_file)
        random_car, random_direction = random_move_algorithm.make_move()

        if game.move_car(random_car, random_direction) is not False:
            history.add_move(random_car, random_direction)
            history.add_board(game.get_board())

        screen.fill((127, 127, 127))
        # For every move, the pygame board is updated.
        game.draw_board(screen)
        pygame.display.flip()

        clock.tick(15)

    pygame.display.quit()

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

    if select_algorithm in ['1', '2', '3']:
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

    # print(history.get_board_history())
    
    # Add to list of algorithms used and their average moves made
    algorithms_used_and_their_average_moves[select_algorithm] = average_moves

    print(f"\nThe average amount of moves needed for {number_of_games} games was {average_moves} moves, and {average_loops} game loops")

def astar_algorithm():

    # pick board and thus its filepath
    available_board_dictionary = available_boards()
    board_pick = str
    while board_pick not in available_board_dictionary:
        board_pick = str(input("Which board will you pick? "))
    file_path = available_board_dictionary[board_pick]

    game_file = GameFile(file_path)
    game = GameBoard(game_file)
    
    game.get_board_for_player()

    # start timer for data here
    start_time = timeit.default_timer()

    astar = Astar(game).run()

    visual = GameBoard(game_file)

    # Pygame initialization
    pygame.init()
    rows = len(game._board)
    cols = len(game._board[0])
    screen = pygame.display.set_mode((cols * 50, rows * 50))
    pygame.display.set_caption("Rush-Hour Board")
    clock = pygame.time.Clock() 

    for move in astar[0]:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        print(f"Move car {move[0]} in direction {move[1]}")
        visual.move_car(move[0], move[1])
        screen.fill((127, 127, 127))
        visual.draw_board(screen)
        pygame.display.flip()

        clock.tick(15)

    pygame.quit()
    
def breadth_first_search():

    # pick board and thus its filepath
    available_board_dictionary = available_boards()
    board_pick = str
    while board_pick not in available_board_dictionary:
        board_pick = str(input("Which board will you pick? "))
    file_path = available_board_dictionary[board_pick]

    game_file = GameFile(file_path)
    game = GameBoard(game_file)
    
    game.get_board_for_player()

    # start timer for data here
    start_time = timeit.default_timer()

    bfs = BFS(game).run()

    # end timer for data here
    end_time = timeit.default_timer()
    compute_time = end_time - start_time
    print(f"It took this algorithm {compute_time} seconds to compute a solution.")

    # These are the results:
    solution_path, visited_states_count = bfs  # Run BFS
    print(f"results: \n solution_path = {len(solution_path)}\n visited_states_count: {visited_states_count}")

    # Store data in a CSV file
    output_file_path = "data/algoritmen_data.csv"
    with open(output_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["Algorithm", "Board", "Compute Time", "Solution Path Length", "Visited States Count"])
        writer.writerow(["BFS", file_path, compute_time, len(solution_path), visited_states_count])

    print(f"Results saved in {output_file_path}")


def depth_first_search():

    # pick board and thus its filepath
    available_board_dictionary = available_boards()
    board_pick = str
    while board_pick not in available_board_dictionary:
        board_pick = str(input("Which board will you pick? "))    
    file_path = available_board_dictionary[board_pick]

    game_file = GameFile(file_path)
    game = GameBoard(game_file)
    
    game.get_board_for_player()

    # start timer for data here
    start_time = timeit.default_timer()

    dfs = DFS(game).run()

    # end timer for data here
    end_time = timeit.default_timer()
    compute_time = end_time - start_time
    print(f"It took this algorithm {compute_time} seconds to compute a solution.")

    # These are the results:
    solution_path, visited_states_count = dfs  # Run DFS
    print(f"results: \n solution_path = {len(solution_path)}\n visited_states_count: {visited_states_count}")

    # Store data in a CSV file
    output_file_path = "data/algoritmen_data.csv"
    with open(output_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(["Algorithm", "Board", "Compute Time", "Solution Path Length", "Visited States Count"])
        writer.writerow(["DFS", file_path, compute_time, len(solution_path), visited_states_count])

    print(f"Results saved in {output_file_path}")

def Joosts_test_paradijs():
    file_path = 'data/Rushhour6x6_1.csv'
    game_file = GameFile(file_path)

    game = GameBoard(game_file)
    bfs = BFS(game)
    
    results = bfs.run()
    print(len(results[0]), results[1])

    bfs.csv_output()


def DFS_test():

    file_path = 'data/Rushhour6x6_1.csv'
    game_file = GameFile(file_path)

    game = GameBoard(game_file)
    dfs_instance = DFS(game)

    start_time = timeit.default_timer()

    # These are the results:
    solution_path, visited_states_count = dfs_instance.run()  # Run DFS
    print(f"results: {len(solution_path)}, {visited_states_count}")

    # Export the compressed DFS move history to a CSV file
    dfs_instance.csv_output()  

    end_time = timeit.default_timer()
    print(f"It took this algorithm {end_time - start_time} seconds to compute a solution.")


def print_in_barchart(data_dict):
    """
    Prints a barchart with matplotlib
    """
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

def compare_BFS_DFS(csv_data_file):
    """
    Reads the data file made by running algo_comparisons()
    Makes a barchart from it?....
    """
    # Open the CSV file for reading
    with open(csv_data_file, mode='r') as file:
        reader = csv.reader(file)

        # Read and print each row in the CSV file
        for row in reader:
            print(row)


def main():

    while True:

        mode = str
        while mode not in ['v', 'e', 'b', 'd']:
            mode = input("\nDo you want to run the game in the Visual mode, or in the Experiment mode, BFS, or DFS? (v/e/b/d) ").lower()
    
        if mode == 'v':
            visual()
        elif mode == 'e':
            experiment()
        elif mode == 'b':
            breadth_first_search()
        elif mode == 'd':
            depth_first_search()

        continu = str
        while continu not in ['q', 'c']:
            continu = input("\nDo you want to continue, or quit? (c/q) ")

        if continu == 'q':
            # prints into a barchart
            # print_in_barchart(algorithms_used_and_their_average_moves)
            compare_BFS_DFS()
            break
        elif continu == 'c':
            continue

def algo_comparisons():

    # list of BFS and DFS results! Data om te printen
    bfs_dfs_data = {}

    while True:

        mode = str
        while mode not in ['b', 'd', 'q']:
            mode = input("\nbfs or dfs or q?").lower()
        if mode == 'b':
            breadth_first_search()
        elif mode == 'd':
            depth_first_search()
        elif mode == 'q':
            csv_data_file = 'data/algoritmen_data.csv'
            compare_BFS_DFS(csv_data_file)

        continu = str
        while continu not in ['q', 'c']:
            continu = input("\nDo you want to continue, or quit? (c/q) ")

        if continu == 'q':
            # prints into a barchart
            # print_in_barchart(algorithms_used_and_their_average_moves)
            csv_data_file = 'data/algoritmen_data.csv'
            compare_BFS_DFS(csv_data_file)
            break
        elif continu == 'c':
            continue


def Joosts_test_paradijs():
    file_path = 'data/Rushhour6x6_3.csv'
    game_file = GameFile(file_path)
    game = GameBoard(game_file)
    astar = BFS(game)
    print(game.get_board_for_player())
    results = astar.run()
    print(game.get_board_for_player())
    print(f"solution found with {len(results[0])} moves, boards visited: {results[1]}")




if __name__ == '__main__':

    print("Choose an option:")
    print("1. Joost's Test Paradijs")
    print("2. DFS Test")
    print("3. Main")
    print("4. Algo_comparisons")
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        Joosts_test_paradijs()
    elif choice == '2':
        DFS_test()
    elif choice == '3':
        main()
    elif choice == '4':
        algo_comparisons()
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")



# pygames add to depth_first_search:

    # visual = GameBoard(game_file)

    # Pygame initialization
    # pygame.init()
    # rows = len(game._board)
    # cols = len(game._board[0])
    # screen = pygame.display.set_mode((cols * 50, rows * 50))
    # pygame.display.set_caption("Rush-Hour Board")
    # clock = pygame.time.Clock() 

    # for move in dfs[0]:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             return

    #     print(f"Move car {move[0]} in direction {move[1]}")
    #     visual.move_car(move[0], move[1])
    #     screen.fill((127, 127, 127))
    #     visual.draw_board(screen)
    #     pygame.display.flip()

    #     clock.tick(15)

    # pygame.quit()
