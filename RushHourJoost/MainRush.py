from GameBoardClass import GameBoard


if __name__ == '__main__':
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