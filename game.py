import pygame

from board import Board
from selector import Selector

class Game:
    def __init__(self):
        self.screen_res = pygame.Vector2(1280, 720)
        self.screen = pygame.display.set_mode(self.screen_res)

        self.units_texture = pygame.image.load("units.png")
        self.sprites = [(1, 0), (0, 6), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13)]
        self.selection = self.sprites[0]

        self.board = Board(self, 10, 10, 8, 8)
        self.selector = Selector(self, 600, 10, 2, 4)
        self.selector.updateSprite(self.sprites)

        self.running = True
        self.clock = pygame.time.Clock()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)

                    if ((x >= self.board.pos.x) and (x < self.board.pos.x + self.board.window_size.x)) \
                            and ((y >= self.board.pos.y) and (y < self.board.pos.y + self.board.window_size.y)):
                                self.board.addSprite(x, y)

                    elif ((x >= self.selector.pos.x) and (x < self.selector.pos.x + self.selector.window_size.x)) \
                            and ((y >= self.selector.pos.y) and (y < self.selector.pos.y + self.selector.window_size.y)):
                                self.selector.selectSprite(x, y)

                elif event.button == 3:
                    x, y = pygame.mouse.get_pos()
                    print(x, y)

                    if ((x >= self.board.pos.x) and (x < self.board.pos.x + self.board.window_size.x)) \
                            and ((y >= self.board.pos.y) and (y < self.board.pos.y + self.board.window_size.y)):
                                self.board.removeSprite(x, y)

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        self.board.draw()
        self.selector.draw()

        pygame.display.update()

    def run(self):
        while self.running:
            self.eventLoop()
            self.update()
            self.render()
            self.clock.tick(60)
