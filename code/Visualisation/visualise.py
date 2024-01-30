import pygame

class Visualisers:

    def draw_colors(self, value):
        # The colors for the squares on the Pygame board
        self.color_values = {
            'A': (0, 0, 0),
            'B': (0, 0, 85),
            'C': (0, 0, 170),
            'D': (0, 0, 255),
            'E': (0, 85, 0),
            'F': (0, 170, 0),
            'G': (255, 170, 0),
            'H': (0, 0, 127),
            'I': (0, 127, 0),
            'J': (0, 85, 85),
            'K': (0, 85, 127),
            'L': (0, 127, 85),
            'M': (0, 85, 255),
            'N': (0, 255, 85),
            'O': (0, 255, 0),
            'P': (42, 255, 170),
            'Q': (42, 170, 255),
            'R': (0, 127, 127),
            'S': (0, 255, 255),
            'T': (255, 0, 170),
            'U': (50, 50, 50),
            'V': (150, 150, 150),
            'W': (0, 190, 95),
            'Y': (0, 95, 190),
            'Z': (0, 255, 75),
            'AA': (0, 0, 0),
            'AB': (0, 0, 85),
            'AC': (0, 0, 170),
            'AD': (0, 0, 255),
            'AE': (0, 85, 0),
            'AF': (0, 170, 0),
            'AG': (0, 255, 0),
            'AH': (0, 0, 127),
            'AI': (0, 127, 0),
            'AJ': (0, 85, 85),
            'AK': (0, 85, 127),
            'AL': (0, 127, 85),
            'AM': (0, 85, 255),
            'AN': (0, 255, 85),
            'AO': (255, 170, 0),
            'AP': (42, 255, 170),
            'AQ': (42, 170, 255),
            'AR': (0, 127, 127),
            'AS': (0, 255, 255),
        }

        return self.color_values.get(value)

    # This defines a new board with pygame!
    def draw_board(self, screen):
        
        # These loops decide the size of the code
        for row_index, row in enumerate(self._board):
            for col_index, cell_value in enumerate(row):
                x = col_index * 50
                y = row_index * 50
                # Cell_value determines if a space on the board is a car or not.
                # A cell_value of 0 means that there's no car on a certain spot.
                if cell_value != 0:
                    # Is the cell_value 'X'? The cell is filed with the red car.
                    color = (255, 0, 0) if cell_value == 'X' else (self.draw_colors(cell_value))
                    # New cells are drawn on each board with the appropriate colors.
                    pygame.draw.rect(screen, color, (x, y, 50, 50))
                    pygame.draw.rect(screen, (85, 85, 85), (x, y, 50, 50), 2)

    def iterative_gameplay(paths, file):

        game_file = GameFile(file)
        visual = GameBoard(game_file)

        pygame.init()
        rows = len(visual._board)
        cols = len(visual._board[0])
        screen = pygame.display.set_mode((cols * 50, rows * 50))
        pygame.display.set_caption("Rush-Hour Board")
        clock = pygame.time.Clock() 

        for move in paths:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            visual.move_car(move[0], move[1])
            screen.fill((127, 127, 127))
            visual.draw_board(screen)
            pygame.display.flip()

            clock.tick(15)

        pygame.quit() 
    
