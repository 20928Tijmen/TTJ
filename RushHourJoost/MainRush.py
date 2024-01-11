from GameBoardClass import GameBoard


if __name__ == '__main__':

    validboards = ["Rushhour6x6_1.csv", "Rushhour6x6_2.csv", "Rushhour6x6_3.csv",  "Rushhour9x9_4.csv", "Rushhour9x9_5.csv", "Rushhour9x9_6.csv"]
    print("Available boards:\n\nRushhour6x6_1.csv\nRushhour6x6_2.csv\nRushhour6x6_3.csv\nRushhour9x9_4.csv\nRushhour9x9_5.csv\nRushhour9x9_6.csv\n")
    
    select = 'Selection'
    
    while select not in validboards:
        select = input("Select board: ")
    
    print('\n')

    game = GameBoard(select)
    game.add_cars(select)

    board = game.get_board()
    fancy_board = game.get_board_for_player()

    print(fancy_board)    

    while True:
        letter = input("give car letter:  ")
        direction = int(input("give direction. 1 or -1:  " ))

        game.move_car(letter, direction)

        print(game.get_board_for_player())
