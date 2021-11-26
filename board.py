import pygame
import misc

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

    def update(self):
        """
        This function will update the game board.
        Because I'm lazy and there isn't much time, I wont make a graph algo here.
        Instead, I'll be using some greedy algo with multiple iteration

        Okay, the greedy algo is as such
        1. Iterate through all, if there's an item, move the item in the direction of the arrow.
           This might make the item to stack on top of each other, it'll be fixed later
        2. Iterate again, for each object with source or struct type, do the calculation
           and create new item object as needed
        3. Iterate again through all, this time, remove all stacking item, except the most bottom one

        So, we can assump that each cell has a maximum of one item on top of it.

        Now that I think of it again, I would need to define wether each item is able to receive
        anything from its surrounding in data.json. Life, I guess :")

        Mew :3
        """
        pass

    def draw(self):
        for x in range(int(self.size.x)):
            for y in range(int(self.size.y)):
                cell_pos = pygame.Vector2(x, y).elementwise() * self.cell_size
                misc.drawGrid(self.game.screen, (255, 255, 255), self.pos, cell_pos, self.cell_size, self.window_size)

                position = pygame.Vector2(x, y).elementwise() * self.cell_size
                position = position.elementwise() + self.pos
                self.grid[y][x].draw(self.game.screen, position)
