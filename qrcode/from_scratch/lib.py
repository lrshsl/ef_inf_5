import pygame

BLACK: (int, int, int, int) = (0, 0, 0, 1)
WHITE: (int, int, int, int) = (1, 1, 1, 1)

class Grid:
    screen_size: [int, int] = [800, 800]     # always quadratic!!
    margin: int = 100

    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self.cell_size = (self.screen_size[0] - self.margin) / self.cols

    def eat(self, data) -> None:
        self.data = iter(data)

    def draw(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        #screen.set_caption('qrcode:')
        self.show_window(screen)
    
    def show_window(self, screen) -> None:
        should_quit: bool = False
        while not should_quit:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    should_quit = True
                self.draw_qr(screen)
                pygame.display.flip()
        pygame.quit()

    def draw_qr(self, screen) -> None:
        screen.fill(WHITE)
        rect = pygame.Rect(
            (self.margin, self.margin),
            (self.screen_size[0] - self.margin, self.screen_size[1] - self.margin))
        for _ in range(self.cols):
            for _ in range(self.rows):
                rect.x += self.cell_size
                try:
                    color = BLACK if not next(self.data) else WHITE
                except:
                    pass
                pygame.draw.rect(screen, color, rect)
            rect.x = 0
            rect.y += self.cell_size
