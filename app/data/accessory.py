from dataclasses import dataclass
from item import Item
from skill import Skill

@dataclass
class Accessory(Item):
    usable: bool
    stats: {str: int}
    skill_on_equip: Skill or None
    skill_on_use: Skill or None
