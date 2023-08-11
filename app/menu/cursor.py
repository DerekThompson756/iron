import pygame
from controllers.animation import Animation
from controllers.sprite_sheet import Spritesheet
from controllers.square import give_square

class Cursor(pygame.sprite.Sprite, Animation):
    
    def __init__(self,MAP_SIZE,SQUARE_SIZE):
        super().__init__()
        self.map_size = MAP_SIZE
        self.sqaure_size = SQUARE_SIZE
        self.x = (MAP_SIZE[0] // 2) - 1
        self.y = (MAP_SIZE[1] // 2) - 1
        self.width = SQUARE_SIZE[0]
        self.height = SQUARE_SIZE[1]
        give_square(self)
        spritesheet = Spritesheet("resources/sprites/cursor.png")
        self.sprites = spritesheet.load_strip((0,-1,32,32), 3, -1)
        
        self.current_sprite = 0
        self.img = self.sprites[self.current_sprite]
        self.frame = 1

    def draw(self, display):
        self.update_pos()
        display.blit(self.img, (self.rect.center[0]-self.sqaure_size[0],self.rect.center[1]-self.sqaure_size[1]))

    def update(self):
        self.frame += 1

        if 1 <= self.frame <= 25:
            self.current_sprite = 0
        elif 26 <= self.frame <= 30:
            self.current_sprite = 1
        elif 31 <= self.frame <= 55:
            self.current_sprite = 2
        elif 56 <= self.frame <= 60:
            self.current_sprite = 1

        if self.frame >= 60:
            self.frame = 1
        
        self.img = self.sprites[int(self.current_sprite)]

    def move(self, direction):
        if direction:
            print(direction)
            if direction == 'up':
                if self.y != 0:
                    self.y -= 1
            if direction == 'down':
                if self.y != self.map_size[1]-1:
                    self.y += 1
            if direction == 'left':
                if self.x != 0:
                    self.x -= 1
            if direction == 'right':
                if self.x != self.map_size[0]-1:
                    self.x += 1
        self.update_pos()
        print(self.pos)
        

    def update_pos(self):
        self.abs_x = self.x * self.width
        self.abs_y = self.y * self.height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.selected_unit = None
        self.rect.update(self.abs_x, self.abs_y, self.sqaure_size[0],self.sqaure_size[1])
        
