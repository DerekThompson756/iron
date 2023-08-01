import pygame

class Cursor(pygame.sprite.Sprite):
    
    def __init__(self, map_size, width, height):
        super().__init__()
        self.x = (map_size[0] // 2) - 1
        self.y = (map_size[1] // 2) - 1
        self.width = width
        self.height = height
        self.abs_x = self.x * width
        self.abs_y = self.y * height
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
        display.blit(self.img, self.rect.topleft)

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
                self.y -= 1
            if direction == 'down':
                self.y += 1
            if direction == 'left':
                self.x -= 1
            if direction == 'right':
                self.x += 1
        self.update_pos()
        print(self.pos)

    def update_pos(self):
        self.abs_x = self.x * self.width
        self.abs_y = self.y * self.height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.selected_unit = None
        self.rect.move(self.abs_x, self.abs_y)
