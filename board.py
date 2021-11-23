import pygame

class Board:
    def __init__(self, game, start_x, start_y, tile_x, tile_y):
        self.game = game

        self.cell_size = pygame.Vector2(64, 64)
        self.units_texture = pygame.image.load("units.png")

        self.pos = pygame.Vector2(start_x, start_y)
        self.size = pygame.Vector2(tile_x, tile_y)
        self.grid = [ [Stuff(self, self.game.units_texture) for _ in range(tile_x)] for _ in range(tile_y)]
        self.window_size = self.cell_size.elementwise() * self.size

    def addSprite(self, pos_x, pos_y):
        x = int((pos_x - self.pos.x) / self.cell_size.x)
        y = int((pos_y - self.pos.y) / self.cell_size.y)

        if self.grid[x][y].filled:
            self.grid[x][y].visible = True
        else:
            self.grid[x][y].update(0, 6)

    def removeSprite(self, pos_x, pos_y):
        x = int((pos_x - self.pos.x) / self.cell_size.x)
        y = int((pos_y - self.pos.y) / self.cell_size.y)

        self.grid[x][y].visible = False


    def draw(self):
        for x in range(int(self.size.x)):
            for y in range(int(self.size.y)):
                cell_pos = pygame.Vector2(x, y).elementwise() * self.cell_size
                pygame.draw.line(
                        self.game.screen, (255, 255, 255),
                        (self.pos.x + cell_pos.x, self.pos.y),
                        (self.pos.x + cell_pos.x, self.pos.y + self.window_size.y - 1)
                        )
                pygame.draw.line(
                        self.game.screen, (255, 255, 255),
                        (self.pos.x + cell_pos.x + self.cell_size.x - 1, self.pos.y),
                        (self.pos.x + cell_pos.x + self.cell_size.x - 1, self.pos.y + self.window_size.y - 1)
                        )
                pygame.draw.line(
                        self.game.screen, (255, 255, 255),
                        (self.pos.x, self.pos.y + cell_pos.y),
                        (self.pos.x + self.window_size.x - 1, self.pos.y + cell_pos.y)
                        )
                pygame.draw.line(
                        self.game.screen, (255, 255, 255),
                        (self.pos.x, self.pos.y + cell_pos.y + self.cell_size.y - 1),
                        (self.pos.x + self.window_size.x - 1, self.pos.y + cell_pos.y + self.cell_size.y - 1)
                        )

                if self.grid[x][y].visible:
                    sprite = self.grid[x][y]
                    position = pygame.Vector2(x, y).elementwise() * self.cell_size
                    position = position.elementwise() + self.pos
                    self.game.screen.blit(sprite.texture, position, sprite.texture_rect)

class Stuff:
    def __init__(self, board, texture):
        self.cell_size = board.cell_size
        self.texture = texture
        self.texture_rect = pygame.Rect(0, 0, 0, 0)

        self.padding = board.pos

        self.visible = False
        self.filled = False

    def update(self, pos_x, pos_y):
        texture_pos = pygame.Vector2(pos_x, pos_y).elementwise() * self.cell_size
        print(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))

        self.texture_rect = pygame.Rect(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))
        self.filled = True
        self.visible = True
