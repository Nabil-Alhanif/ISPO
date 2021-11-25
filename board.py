import pygame

from sprite import Sprite

class Board:
    def __init__(self, game, start_x, start_y, tile_x, tile_y):
        self.game = game

        self.cell_size = pygame.Vector2(64, 64)
        self.units_texture = self.game.units_texture

        self.pos = pygame.Vector2(start_x, start_y)
        self.size = pygame.Vector2(tile_x, tile_y)
        self.grid = [ [Sprite(self, self.game.units_texture) for _ in range(tile_x)] for _ in range(tile_y)]
        self.window_size = self.cell_size.elementwise() * self.size

    def addSprite(self, pos_x, pos_y):
        x = int((pos_x - self.pos.x) / self.cell_size.x)
        y = int((pos_y - self.pos.y) / self.cell_size.y)

        self.grid[y][x].update(self.game.selection)

    def removeSprite(self, pos_x, pos_y):
        x = int((pos_x - self.pos.x) / self.cell_size.x)
        y = int((pos_y - self.pos.y) / self.cell_size.y)

        self.grid[y][x].remove(self.grid[y][x].last_data["type"] == "source")

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

                position = pygame.Vector2(x, y).elementwise() * self.cell_size
                position = position.elementwise() + self.pos
                self.grid[y][x].draw(self.game.screen, position)
