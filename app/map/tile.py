import pygame
from controllers.animation import Animation
from controllers.square import give_square

class Tile(pygame.sprite.Sprite, Animation):
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        give_square(self)
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