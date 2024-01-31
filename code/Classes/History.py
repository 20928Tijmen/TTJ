import csv


class History():
    """
    Must make a history! because you want to be able to record the correct path! and for the algorithm its useful!!
    """
    def __init__(self):

        self.move_history: list[(str, int)] = []  # a move is a (letter of car, direction)
        self.board_history: list[list[list]] = []  # the board is a list of lists, so a list of those

        self.previous_move: (str, int) = ()

        self.counter = 0

    def add_move(self, car_letter: object, direction: int) -> None:
        """
        add a move to the move history
        """
        move = (car_letter, direction)
        self.move_history.append(move)
        self.counter += 1

        self.previous_move = move

    def add_board(self, board: list[list]) -> list:
        """
        add a board to the board history
        """
        self.board_history.append(board)

    def get_counter(self) -> int:
        """
        returns the counter number
        """
        return self.counter

    def get_move_history(self) -> list:
        """
        returns the list of previous moves
        """
        return self.move_history

    def get_board_history(self) -> list:
        """
        return the list of previous boards
        """
        return self.board_history

    def go_back(self) -> None:
        """
        makes the last move dissapear of the history and counter
        """
        self.move_history.pop()
        self.counter -= 1

    def get_move_history_compressed(self) -> list:
        """
        Returns a compressed list of move history, summarizing consecutive moves for each car.

        Dit is voorbeeld ouput van de webpage van de case. zie hoe moves bij elkaar opgeteld worden.

        car,move
        A,-1
        B,1
        C,-1
        E,1
        G,2
        J,-1
        I,-1
        X,4

        !!!! een move met 0 is bij random dus dat 1 en -1 achter elkaar gespeeld werden !!!

        Als een auto twee keer dezelfde beweging maakt dan compressed hij dat naar 1 move zeg maar.

        """
        compressed_history = [self.move_history[0]]

        for move in self.move_history[1:]:
            last_move = compressed_history[-1]

            if move[0] == last_move[0]:  # If the current move is for the same car
                new_move = (move[0], last_move[1] + move[1])  # Sum the moves
                compressed_history[-1] = new_move
            else:
                compressed_history.append(move)

        return compressed_history

    def export_compressed_to_csv(self, file_name):
        """
        Exports the compressed move history to a CSV file.
        """
        compressed_history = self.get_move_history_compressed()

        with open(file_name, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['car', 'move'])  # Write the header
            for move in compressed_history:
                writer.writerow(move)

    def export_uncompressed_to_csv(self, file_name):
        """
        Exports the uncompressed move history to a CSV file.
        """
        with open(file_name, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['car', 'move'])  # Write the header
            for move in self.move_history:
                writer.writerow(move)
