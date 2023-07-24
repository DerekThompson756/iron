import pygame

class Tile():
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.occupying_unit = None
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )
        self.tile_name = 'Plains'
        self.stats = []
        self.draw_color = 'green'
        img_path = 'resources/tilesets/village_1/tile_1.png'
        self.img = pygame.image.load(img_path)

    def draw(self, display):
        display.blit(self.img, self.rect.topleft)

    def __str__(self) -> str:
        return self.tile_name + str(self.pos)

    def __repr__(self) -> str:
        return self.tile_name + str(self.pos)