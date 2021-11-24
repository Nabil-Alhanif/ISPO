import pygame

class Sprite:
    def __init__(self, board, texture):
        self.cell_size = board.cell_size
        self.texture = texture
        self.texture_rect = pygame.Rect(0, 0, 0, 0)

        self.pos = pygame.Vector2(0, 0)
        self.padding = board.pos
        self.msg = ""

        self.visible = False
        self.filled = False

    def update(self, pos_x, pos_y, msg=""):
        texture_pos = pygame.Vector2(pos_x, pos_y).elementwise() * self.cell_size
        print(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))

        self.pos = pygame.Vector2(pos_x, pos_y)
        self.msg = msg

        self.texture_rect = pygame.Rect(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))
        self.filled = True
        self.visible = True
