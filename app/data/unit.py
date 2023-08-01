import pygame
from dataclasses import dataclass
from klass import Klass
from affinity import Affinity
from gameStats import Stats
from controllers.animation import Animation

@dataclass
class Unit(pygame.sprite.Sprite, Animation):
    id: str
    name: str
    level: int
    description: str
    klass: Klass
    tags: list()
    stats: Stats 
    weapon_exp: dict()
    inventory: list()
    personal_skills: list()
    spell_list: dict()
    affinity: Affinity


    def draw(self, display):
        display.blit(self.img, self.rect.topleft)
    