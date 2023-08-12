from dataclasses import dataclass


@dataclass
class In_Combat_Stats():
    damage: int
    resist: int
    hit: int
    avoid: int
    crit: int
    dodge: int

