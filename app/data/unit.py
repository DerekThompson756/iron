from dataclasses import dataclass
from klass import Klass
from affinity import Affinity

@dataclass
class Unit():
    id: str
    name: str
    level: int
    description: str
    klass: Klass
    tags: list()
    stats: dict()
    weapon_exp: dict()
    inventory: list()
    personal_skills: list()
    spell_list: dict()
    affinity: Affinity 
    