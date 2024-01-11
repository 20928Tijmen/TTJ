from vehicles import Car, Redcar

class Board():
    """This class represents the gameboard"""

    def __init__(self, filename):
        """
        This will initialize the game board.

        Pre: A valid filename has to be given.
        Post: The board is initialized based on the given file.
        """

        # create list for board information
        self.boardinfo = []

        # read csv excel file
        with open(filename) as file:
            for line in file:
                if line == '\n':
                    file.close()
                    break
                datasplit = line.strip().split(',')

                if datasplit[0].isupper():
                    self.boardinfo.append(datasplit)

            file.close()

        self.gameboard = []

        if '6x6' in filename:
            loop = 6
        elif '9x9' in filename:
            loop = 9
        elif '12x12' in filename:
            loop = 12

        for ro in range(loop):
            row = []
            for til in range(loop):
                row.append('_')
            self.gameboard.append(row)

    def showboard(self):
        """
        This will display the current state of the board.
        Pre: A board needs to have been initialized.
        Post: The current state of the game board is printed.
        """
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[i])):
                print(f" {self.gameboard[i][j]} ", end="")
            print("\n")

class Vehicle():

    def __init__(self, boardinfo, gameboard):
        """
        This initializer will place the vehicles o  n the board.
        Pre: There needs to be an initialized gameboard and info
        on what needs to be placed on the board.
        Post: The vehicles are placed on the board.
        """

        for k in range(len(boardinfo)):
            ro = int(boardinfo[k][3]) - 1
            colu = int(boardinfo[k][2]) - 1
            if boardinfo[k][1] == 'H':
                lengt = int(boardinfo[k][4])
                for l in range(lengt):
                    gameboard[ro][colu + l] = boardinfo[k][0]

            if boardinfo[k][1] == 'V':
                lengt = int(boardinfo[k][4])
                for l in range(lengt):
                    gameboard[ro + l][colu] = boardinfo[k][0]

    def move_vehicle(self, gameboard, car):
        
        for k in range(6):
            for l in range(6):
                if gameboard[k][l] == car:
                    if gameboard[k][l + 1] == car:
                        if gameboard[k][l - 1] == '_':
                            gameboard[k][l - 1] = car
                            gameboard[k][l + 1] = '_'

if __name__ == "__main__":
    
    validboards = ["Rushhour6x6_1.csv", "Rushhour6x6_2.csv", "Rushhour6x6_3.csv",  "Rushhour9x9_4.csv", "Rushhour9x9_5.csv", "Rushhour9x9_6.csv"]
    print("Available boards:\n\nRushhour6x6_1.csv\nRushhour6x6_2.csv\nRushhour6x6_3.csv\nRushhour9x9_4.csv\nRushhour9x9_5.csv\nRushhour9x9_6.csv\n")
    
    select = 'Selection'
    
    while select not in validboards:
        select = input("Select board: ")
    
    print('\n')
    
    rushhour = Board(select)

    vehicles = Vehicle(rushhour.boardinfo, rushhour.gameboard)
    
    rushhour.showboard()

    vehicles.move_vehicle(rushhour.gameboard, "A")
    vehicles.move_vehicle(rushhour.gameboard, "C")

    rushhour.showboard()
