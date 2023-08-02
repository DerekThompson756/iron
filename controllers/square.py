import pygame
from abc import ABC, abstarctmethod
from animation import Animation

class Square(ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = self.x * self.width
        self.abs_y = self.y * self.height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )