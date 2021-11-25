import pygame

class Sprite:
    def __init__(self, board, texture):
        self.cell_size = board.cell_size
        self.texture = texture
        self.texture_rect = pygame.Rect(0, 0, 0, 0)

        self.pos = pygame.Vector2(0, 0)
        self.id = ["base"]
        self.data = {
                "base": {
                    "type":"base",
                    "pos":[0, 0],
                    "name":"base",
                    "text":""
                    }
                }
        self.last_data = self.data["base"]

    def update(self, data):
        print(data)

        print("data type")
        print(data["type"])
        self.remove(data["type"] == "source")

        # Make sure there is no duplicate
        if self.last_data["name"] == data["name"]:
            return

        print("self.data")
        print(self.data)

        self.id.append(data["name"])
        self.data[data["name"]] = data
        self.last_data = data

    def remove(self, delete_source = False):

        key = self.id[-1]

        # base must exist
        if self.data[key]["type"] == "base":
            return

        if not delete_source and self.data[key]["type"] == "source":
            return

        while True:
            print("deleting ", key, self.data[key])

            self.id.pop()
            del self.data[key]
            key = self.id[-1]

            if self.data[key]["type"] == "base":
                break

            if not delete_source and self.data[key]["type"] == "source":
                break

        key = self.id[-1]
        self.last_data = self.data[key]

    def draw(self, screen, position):
        for key in self.id:
            pos_x, pos_y = self.data[key]["pos"]

            texture_pos = pygame.Vector2(pos_x, pos_y).elementwise() * self.cell_size
            #print(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))

            texture_rect = pygame.Rect(int(texture_pos.x), int(texture_pos.y), int(self.cell_size.x), int(self.cell_size.y))

            screen.blit(self.texture, position, texture_rect)
