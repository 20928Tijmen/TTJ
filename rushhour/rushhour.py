from vehicles import Car, Truck, Redcar

class Board():
    """This class represents the gameboard"""

    def __init__(self, filename):
        """
        This will initialize the game board.

        Pre: A valid filename has to be given.
        Post: The board is initialized based on the given file.
        """

        self.boardinfo = []

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

        for k in range(len(self.boardinfo)):
            ro = int(self.boardinfo[k][3]) - 1
            colu = int(self.boardinfo[k][2]) - 1
            if self.boardinfo[k][1] == 'H':
                lengt = int(self.boardinfo[k][4])
                for l in range(lengt):
                    self.gameboard[ro][colu + l] = self.boardinfo[k][0]

            if self.boardinfo[k][1] == 'V':
                lengt = int(self.boardinfo[k][4])
                for l in range(lengt):
                    self.gameboard[ro + l][colu] = self.boardinfo[k][0]

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

if __name__ == "__main__":
    validboards = ["Rushhour6x6_1.csv", "Rushhour6x6_2.csv", "Rushhour6x6_3.csv",  "Rushhour9x9_4.csv", "Rushhour9x9_5.csv", "Rushhour9x9_6.csv"]
    print("Available boards:\n\nRushhour6x6_1.csv\nRushhour6x6_2.csv\nRushhour6x6_3.csv\nRushhour9x9_4.csv\nRushhour9x9_5.csv\nRushhour9x9_6.csv\n")
    select = 'Selection'
    
    while select not in validboards:
        select = input("Select board: ")
    
    print('\n')
    rushhour = Board(select)
    
    rushhour.showboard()
