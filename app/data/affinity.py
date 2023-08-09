from dataclasses import dataclass
from app.data.in_combat_stats import In_Combat_Stats

@dataclass
class Affinity():
    id: int
    name: str
    description: str
    bonuses: In_Combat_Stats
    icon_path: str # file path for icon
    