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

        for i in range(6):
            row = []
            for j in range(1, 7):
                row.append('_')
            self.gameboard.append(row)

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

    rushhour = Board(select)

    print(rushhour.boardinfo)

    rushhour.showboard()