import pygame

class Game():
    def __init__(self):
        pygame.init()

        self.cellSize = pygame.Vector2(64, 64)
        self.worldSize = pygame.Vector2(16, 10)

        windowSize = self.worldSize.elementwise() * self.cellSize
        self.window = pygame.display.set_mode((int(windowSize.x), int(windowSize.y)))

        self.clock = pygame.time.Clock()
        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    break

    def update(self):
        pass

    def render(self):
        self.window.fill((0, 0, 0))
        self.drawGrid()

        pygame.display.update()

    def drawGrid(self):
        for x in range(int(self.worldSize.x)):
            for y in range(int(self.worldSize.y)):
                pos = pygame.Vector2(x, y).elementwise() * self.cellSize
                windowSize = self.worldSize.elementwise() * self.cellSize
                pygame.draw.line(self.window, (255, 255, 255), (pos.x, 0), (pos.x, windowSize.y))
                pygame.draw.line(self.window, (255, 255, 255), (pos.x + self.cellSize.x - 1, 0), (pos.x + self.cellSize.x - 1, windowSize.y))
                pygame.draw.line(self.window, (255, 255, 255), (0, pos.y), (windowSize.x, pos.y))
                pygame.draw.line(self.window, (255, 255, 255), (0, pos.y + self.cellSize.y - 1), (windowSize.x, pos.y + self.cellSize.y - 1))

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(60)

game = Game()
game.run()

pygame.quit()
