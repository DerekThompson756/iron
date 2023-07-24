from dataclasses import dataclass


@dataclass
class Chapter():
    chapter_id:str
    name:str
    music:str
    objective_description:str
    win_condition:str
    loss_condition:str
 