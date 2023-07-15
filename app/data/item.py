from dataclasses import dataclass
from abc import ABC

@dataclass
class Item(ABC):
    item_id: str
    item_name: str
    description: str
    uses: int
