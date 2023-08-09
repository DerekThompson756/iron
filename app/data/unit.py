import pygame
from dataclasses import dataclass
from klass import Klass
from affinity import Affinity
from gameStats import Stats
from controllers.animation import Animation
from app.data.skill import Skill
from app.data.weapon import Weapon

@dataclass
class Unit(pygame.sprite.Sprite, Animation):
    id: str
    name: str
    level: int
    description: str
    klass: Klass
    tags: list()
    stats: Stats 
    weapon_exp: {str in ("Sword", "Lance", "Bow", "White", "Black", "Monster", "Other"): int}
    inventory: list()
    personal_skills: [Skill] or []
    spell_list: [Weapon]
    affinity: Affinity


    def draw(self, display):
        display.blit(self.img, self.rect.topleft)
    