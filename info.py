import pygame
import misc

class Info:
    def __init__(self, game, start_x, start_y, size_x, size_y):
        self.game = game

        self.pos = pygame.Vector2(start_x, start_y)
        self.window_size = pygame.Vector2(size_x, size_y)

        self.msg = "This is a very very very very long message. Well it's not that long, but now it is."

        self.rect = pygame.Rect(start_x, start_y, size_x, size_y)

    def draw(self):
        pygame.draw.line(
                self.game.screen, (255, 255, 255),
                (self.pos.x, self.pos.y),
                (self.pos.x, self.pos.y + self.window_size.y - 1)
                )
        pygame.draw.line(
                self.game.screen, (255, 255, 255),
                (self.pos.x + self.window_size.x - 1, self.pos.y),
                (self.pos.x + self.window_size.x - 1, self.pos.y + self.window_size.y - 1)
                )
        pygame.draw.line(
                self.game.screen, (255, 255, 255),
                (self.pos.x, self.pos.y),
                (self.pos.x + self.window_size.x - 1, self.pos.y)
                )
        pygame.draw.line(
                self.game.screen, (255, 255, 255),
                (self.pos.x, self.pos.y + self.window_size.y - 1),
                (self.pos.x + self.window_size.x - 1, self.pos.y + self.window_size.y - 1)
                )
        misc.drawText(self.game.screen, self.msg, (255, 255, 255), self.rect, pygame.font.SysFont("monospace", 20))
