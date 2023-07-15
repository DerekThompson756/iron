from dataclasses import dataclass
from item import Item

@dataclass
class Accessory(Item):
    usable: bool
    stats: dict
    skill_on_equip: Skill
    skill_on_use: Skill
