import pygame
import misc

from sprite import Sprite

class Selector:
    def __init__(self, game, start_x, start_y, tile_x, tile_y):
        self.game = game

        self.cell_size = pygame.Vector2(64, 64)
        self.units_texture = self.game.units_texture
        self.sprites = {}

        self.pos = pygame.Vector2(start_x, start_y)
        self.size = pygame.Vector2(tile_x, tile_y)
        self.grid = [ [Sprite(self, self.game.units_texture) for _ in range(tile_x)] for _ in range(tile_y)]
        self.window_size = self.size.elementwise() * self.cell_size

    def updateSprite(self, sprites):
        self.sprites = sprites

        x, y = 0, 0
        print("Seeding data")
        for data in sprites:
            # Check if the sprite is selectable
            if self.sprites[data]["selectable"] == "no":
                continue

            self.grid[y][x].update(self.sprites[data], True)
            print(x, y)

            print(self.grid[y][x].data)

            x += 1
            if x >= self.size.x:
                x = 0
                y += 1

            if y >= self.size.y:
                break

    def selectSprite(self, pos_x, pos_y):
        x = int((pos_x - self.pos.x) / self.cell_size.x)
        y = int((pos_y - self.pos.y) / self.cell_size.y)

        self.game.selection = self.grid[y][x].last_data
        self.game.info.msg = self.grid[y][x].last_data["text"]

    def draw(self):
        for x in range(int(self.size.x)):
            for y in range(int(self.size.y)):
                cell_pos = pygame.Vector2(x, y).elementwise() * self.cell_size
                misc.drawGrid(self.game.screen, (255, 255, 255), self.pos, cell_pos, self.cell_size, self.window_size)

                position = pygame.Vector2(x, y).elementwise() * self.cell_size
                position = position.elementwise() + self.pos
                self.grid[y][x].draw(self.game.screen, position)
