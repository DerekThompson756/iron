import pygame


class Cursor(pygame.sprite.Sprite):
    
    def __init__(self,MAP_SIZE,SQUARE_SIZE):
        super().__init__()
        self.map_size = MAP_SIZE
        self.sqaure_size = SQUARE_SIZE
        self.x = (MAP_SIZE[0] // 2) - 1
        self.y = (MAP_SIZE[1] // 2) - 1
        self.width = SQUARE_SIZE[0]
        self.height = SQUARE_SIZE[1]
        self.abs_x = self.x * self.width
        self.abs_y = self.y * self.height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.selected_unit = None
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )
        img_path = 'resources/cursor/'
        self.sprites = [pygame.image.load(img_path + 'cursor_1.png'),
                    pygame.image.load(img_path + 'cursor_2.png'),
                    pygame.image.load(img_path + 'cursor_3.png')]
        self.current_sprite = 0
        self.img = self.sprites[self.current_sprite]
        self.anim = 1

    def draw(self, display):
        self.update_pos()
        display.blit(self.img, (self.rect.topleft[0]-self.sqaure_size[0],self.rect.topleft[1]-self.sqaure_size[1]))

    def update(self):
        self.anim += 1

        if 1 <= self.anim <= 25:
            self.current_sprite = 0
        elif 26 <= self.anim <= 30:
            self.current_sprite = 1
        elif 31 <= self.anim <= 55:
            self.current_sprite = 2
        elif 56 <= self.anim <= 60:
            self.current_sprite = 1

        if self.anim >= 60:
            self.anim = 1
        
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
        
