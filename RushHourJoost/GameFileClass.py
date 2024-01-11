import os
import re # (REGEX!! gekke throwback naar DataRepresentaties)

class GameFile:
    '''
    Door deze class kan je dus makkelijk een hele gamefile doorpasen
    dus je kan dan makkelijk gamefile.board_size opvragen
    voorbeelden:
    - in _add_cars() kan je open(game.path, 'r') doen
    - in _create_empty_board kan je: for row in range(game.board_size)
    - game.number kan je gebruiken in main voor spel keuze
    
    + Hiermee kunnen we later wellicht makkelijk de algorithmes door alle games heen laten runnen
    + en dan met bijvoorbeel een self.Fastest_solve of self.time_to_solve alle statistieken bijhouden voor elke game BIJ de game
    
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
        # kijk in self.path naar "Rushhour(1+ digits op deze plek)x(1+ digits op deze plek)"


    def _set_board_number(self) -> str:
        return re.search(r'(\d+).csv$', self.path).group(1)
        # Gebruik regex om het bord nummer direct uit de path te halen
        # uitleg regex:
        # $ betekend dat daar het einde is, en weer is de (\d+) dat je 1+ getallen zoekt op die plek
        # echt top spul dit
    
    def _read_car_data(self) -> list[tuple[str, str, int, int, int]]:
        car_data = []
        with open(self.path, 'r') as file:
            next(file)  # Skip the header line
            for line in file:
                name, orientation, col, row, length = line.strip().split(',')
                car_data.append((name, orientation, int(row), int(col), int(length)))
        return car_data





if __name__ == '__main__':

    folder_path = 'RushHourJoost/data'

    game_file_LIST = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        game_file = GameFile(file_path)

        game_file_LIST.append(game_file)

def Create_List_of_GameFile_Objects_From_Folder(folder_path):

    game_file_list = []

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        
        game_file = GameFile(file_path)

        game_file_list.append(game_file)

    return game_file_list