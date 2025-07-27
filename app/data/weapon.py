from dataclasses import dataclass
from app.data.item import Item
from app.data.skill import Skill
from app.data.stats import Stats
from app.data.in_combat_stats import In_Combat_Stats


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
    stat_changes: Stats
    in_combat_changes: In_Combat_Stats
    hp_cost: int or None
    skill_on_equip: Skill or None
    skill_on_hit: Skill or None
    skill_on_use: Skill or None