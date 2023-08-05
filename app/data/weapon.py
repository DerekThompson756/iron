from dataclasses import dataclass
from item import Item
from skill import Skill


@dataclass
class Weapon(Item):
    target: str in ("enemy", "ally")
    range: (int, int)
    damage: int
    hit: int
    crit: int or None
    weight: int
    weapon_exp: int
    weapon_type: str in ("Sword", "Lance", "Bow", "White", "Black", "Monster", "Other")
    damage_calc: str in ("default", "magic", "magic_at_range")
    hit_calc: str in ("default", "magic")
    stat_changes: str
    hp_cost: int or None
    skill_on_equip: Skill or None
    skill_on_hit: Skill or None
    skill_on_use: Skill or None