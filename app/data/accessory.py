from dataclasses import dataclass
from item import Item
from skill import Skill
from app.data.stats import Stats

@dataclass
class Accessory(Item):
    usable: bool
    stats: Stats
    skill_on_equip: Skill or None
    skill_on_use: Skill or None
