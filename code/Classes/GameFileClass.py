import re # (REGEX!! gekke throwback naar DataRepresentaties)

class GameFile:
    '''
    Represents a game file for the Rush Hour game, containing board and car information.
    Picture this class as the cards in the box of the game with the board setups on them

    input:
    path: string = this is the path to the board csv files

    Attributes
    path: string = this is the path to the board csv files
    board_size: str = the width of the board
    number: int = boards of same width have differnt numbers
    car_info = all data from the csv file
    '''
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.board_size: str = self._set_board_size()
        self.number: str = self._set_board_number()
        self.car_info = self._read_car_data()

    def _set_board_size(self) -> str:
        return re.search(r'(\d+)x\d+_', self.path).group(1)
        # Gebruik regex om de size direct uit de path te plukken
        # uitleg regex: 
        # kijk in self.path naar \d+, 1 op meer digits, opgevolgd door een x, dus de dimensions

    def _set_board_number(self) -> str:
        return re.search(r'(\d+).csv$', self.path).group(1)
        # Gebruik regex om het bord nummer direct uit de path te halen
        # uitleg regex:
        # $ betekend dat daar het einde is, en weer is de (\d+) dat je 1+ getallen zoekt op die plek
        # echt top spul dit
    
    def _read_car_data(self) -> list[tuple[str, str, int, int, int]]:
        """
        Reads car data from the CSV file specified in the path attribute.
        The data is read from the CSV file and stored in car_info
        format: (name, orientation, row, column, length).
        """
        car_data = []
        with open(self.path, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                name, orientation, col, row, length = line.strip().split(',')
                car_data.append((name, orientation, int(row), int(col), int(length)))
        return car_data

    def get_car_names(self) -> list[str]:
        """
        Return a list of just the names of the cars in that game
        """
        return [car[0] for car in self.car_info]
