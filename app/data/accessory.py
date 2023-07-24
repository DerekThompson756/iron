from dataclasses import dataclass
from item import Item
from skill import Skill

@dataclass
class Accessory(Item):
    usable: bool
    stats: dict #(str; int)
    skill_on_equip: Skill #nullable
    skill_on_use: Skill #nullable
