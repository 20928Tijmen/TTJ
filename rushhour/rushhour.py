from vehicles import Car, Truck, Redcar

class Board():

    def __init__(self, filename):

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

        for ro in range(6):
            row = []
            for til in range(6):
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
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[i])):
                print(f" {self.gameboard[i][j]} ", end="")
            print("\n")

if __name__ == "__main__":
    validboards = ["Rushhour6x6_1.csv", "Rushhour6x6_2.csv", "Rushhour6x6_3.csv"]
    print("Available boards:\n\nRushhour6x6_1.csv\nRushhour6x6_2.csv\nRushhour6x6_3.csv\n")
    select = 'Selection'
    
    while select not in validboards:
        select = input("Select board: ")
    
    print('\n')
    rushhour = Board(select)
    
    rushhour.showboard()
