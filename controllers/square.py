import pygame


def give_square(obj):
        obj.abs_x = obj.x * obj.width
        obj.abs_y = obj.y * obj.height
        obj.pos = (obj.x, obj.y)
        obj.abs_pos = (obj.abs_x, obj.abs_y)
        obj.rect = pygame.Rect(
            obj.abs_x,
            obj.abs_y,
            obj.width,
            obj.height
        )