from dataclasses import dataclass
from controllers.animation import Animation
from app.data.stats import Stats
from app.data.growths import Growths
from app.data.skill import Skill


@dataclass
class Klass(Animation):
    id: int
    name: str
    description: str
    tags: list()
    base_stats: Stats
    max_stats: Stats
    generic_growth_rates: Growths
    class_skills: [Skill] or []
    base_weapon_exp: {str in ("Sword", "Lance", "Bow", "White", "Black", "Monster", "Other"): int}
    movement_cost: None # Need to figure out how to handle movement costs based on class and tile
    generic_enemy_portrait: str # file path to img
    map_sprite: str # file path to img
    combat_anim: str # file path to img
