import pygame

FPS: int = 60

BLACK: (int, int, int) = 0, 0, 0
WHITE: (int, int, int) = 200, 200, 200, 255

BG_COLOR: (int, int, int) = 100, 100, 100


class Grid:
    """ Draws some data on a screen using quadratic cells
        It was created as a utility class for drawing QR codes
    """

    screen_size: [int, int] = [800, 800]   # Size of window in pixel
    margin: int = 100                      # Margin in pixel

    def __init__(self, data: list, rows: int, cols: int) -> None:
        """ Konstructor for 'Grid' """

        # Extract size of list
        self.rows = rows
        self.cols = cols

        # Store data as flat list
        if type(data[0]) == list:
            self.data = [e for sublist in data for e in sublist]
        else:
            self.data = data

        # Calculate cell size
        self.cell_size = min(
            (self.screen_size[0] - self.margin * 2) / self.cols,
            (self.screen_size[1] - self.margin * 2) / self.rows
        )


    def draw(self) -> None:
        """ Draws the QR-Code stored in self.data on a new screen """

        # Set up pygame window
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)

        # Finally draw self.data..
        self.show_window(screen)


    def show_window(self, screen) -> None:
        """ Runs the main loop """
        clock = pygame.time.Clock()

        # Loop until window is closed
        should_quit: bool = False
        while not should_quit:

            # Quit if user wants that
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    should_quit = True

            # Clear background
            screen.fill(BG_COLOR)

            # Draw the QR code
            self.draw_qr(screen)

            # Refresh display
            pygame.display.flip()

            # Wait to keep FPS
            clock.tick(FPS)

        # Finally close the window
        pygame.quit()


    def draw_qr(self, screen) -> None:
        """ Actually draws the data (most likely a QR code) to 'screen' """

        # Set up iterator over self.data
        data_iter = iter(self.data)

        # Set up a rectangle on top left corner
        rect = pygame.Rect(
            (self.margin, self.margin),
            (self.cell_size, self.cell_size))

        # walk through all cell positions
        for _ in range(self.rows):
            for _ in range(self.cols):

                # Move rectangle to next cell
                rect.x += self.cell_size

                # Set color of rectangle
                bit = next(data_iter)
                # color = BLACK if not bit else WHITE
                if bit == 0: color = BLACK
                if bit == 1: color = WHITE
                if bit == 2: color = (150, 150, 150)

                # Draw the rectangle
                pygame.draw.rect(screen, color, rect)

            # Move rectangle to next line
            rect.x = self.margin
            rect.y += self.cell_size

