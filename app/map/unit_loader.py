import pygame
from dataclasses import dataclass
from app.data.unit import Unit
from controllers.animation import Animation
from controllers.square import Square
from app.data.klass import Klass
from app.data.stats import Stats
from app.data.affinity import Affinity

class Unit_Loader():
    def __init__(self):
        self.player_units = []
        self.enemy_units = []
        self.other_units = []

    def read_unit(self, chapter):
        #This will be connected to the json database
        #For now it will create units on its own
        #unit = Unit("0", "Duck", 1, "A very cool dude", Klass(), [], Stats(), {}, [], [], {}, Affinity())
        placed_unit = Placed_Unit(None, None, 0, 0, 0, 0, True)
        self.load_unit(placed_unit, "player")
        print(self.player_units)

    def load_unit(self, unit, faction):
        if faction == "player":
            self.player_units.append(unit)
        elif faction == "enemy":
            self.enemy_units.append(unit)
        elif faction == "other":
            self.other_units.append(unit)

    def find_unit(self, unit_name):
        for unit in self.player_units:
            if unit_name == unit.name:
                return (unit, 'player')
        for unit in self.enemy_units:
            if unit_name == unit.name:
                return (unit, 'enemy')
        for unit in self.other_units:
            if unit_name == unit.name:
                return (unit, 'other')


@dataclass
class Placed_Unit(pygame.sprite.Sprite, Square):
    unit: Unit
    commander: Unit
    #All ai attributes should be set to 0 for player units for consistancy
    action_ai: int #Lookup table will be needed for these in the future
    movement_ai: int 
    target_ai: int
    recover_ai: int 
    retreat_ai: bool #Will move in recovery mode or not

    def move():
        pass
