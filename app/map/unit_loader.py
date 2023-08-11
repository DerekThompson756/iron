import pygame
from controllers.sprite_sheet import Spritesheet
from app.data.unit import Unit
from controllers.animation import Animation
from controllers.square import give_square
from app.data.klass import Klass
from app.data.stats import Stats
from app.data.affinity import Affinity

class Unit_Loader():
    """
    A class used to contained all of the placed units for the map

    ...

    Attributes
    ----------
    player_units : Placed_Unit[]
        list of player units

    enemy_units : Placed_Unit[]
        list of enemy units

    player_units : Placed_Unit[]
        list of other units

    Methods
    -------
    read_unit(chapter: int)
        reads units from json database and loads tham into the map based on
        chapter id - At the moment creates units from scratch
    
    load_unit(unit: Placed_Unit, faction: str)
        places unit into the appropriate Placed_Unit list

    find_unit(unit_name) -> (Placed_Unit, str)
        searches Placed_Unit lists and return the Placed_Unit and its faction
        name based on Unit.name
    """

    def __init__(self):
        self.player_units = []
        self.enemy_units = []
        self.other_units = []

    def read_unit(self, chapter):
        #This will be connected to the json database
        #For now it will create units on its own
        #unit = Unit("0", "Duck", 1, "A very cool dude", Klass(), [], Stats(), {}, [], [], {}, Affinity())
        placed_unit = Placed_Unit(None, None, 0, 0, 0, 0, True, 5, 5, 16, 16)
        self.load_unit(placed_unit, "player")
        print("Units loaded:", self.player_units)

    def load_unit(self, unit, faction):
        if faction == "player":
            self.player_units.append(unit)
        elif faction == "enemy":
            self.enemy_units.append(unit)
        elif faction == "other":
            self.other_units.append(unit)

    def find_unit(self, unit_name):
        for unit in self.player_units:
            if unit_name == unit.name:
                return (unit, 'player')
        for unit in self.enemy_units:
            if unit_name == unit.name:
                return (unit, 'enemy')
        for unit in self.other_units:
            if unit_name == unit.name:
                return (unit, 'other')



class Placed_Unit(pygame.sprite.Sprite, Animation):
    """
    A class used to contained all of the placed units for the map

    ...

    Attributes
    ----------
    unit: Unit
        The Unit object that contains data

    commander: Unit or None
        A Unit object to be used for AI descisions

    action_ai: int
        determines how the placed unit will act,
        if player set to 0

    movement_ai: int
        determines how the placed unit will move, 
        if player set to 0

    target_ai: int
        determines how the placed unit will target enemies/allies, 
        if player set to 0

    recover_ai: int
        determines how the placed unit will act in recovery mode,
        if player set to 0

    retreat_ai: bool
        determines if the unit will move when using a healing item,
        if player set to False

    x: int
        starting x position of the unit

    y: int
        starting y position of the unit

    width: int
        width of the unit space in pixels

    height: int
        height of the unit space in pixels


    Methods
    -------
    read_klass_anim(klass: Klass)
        sets Animation attributes based on Unit's klass
        - At the moment create data from scratch


    draw(display)
        draws Placed_Unit to display

    update()
        updates frame count for Animation and makes any nessisary changes

    move(x: int, y: int)
        moves Placed_Unit to specified coordinates on the grid
    """

    def __init__(self,unit,commander, action_ai, movement_ai,target_ai,recover_ai,retreat_ai,x,y,width,height) -> None:
        super().__init__()
        self.unit : Unit = unit
        self.commander: Unit or None = commander  
        #All ai attributes should be set to 0 for player units for consistancy
        self.action_ai: int = action_ai#Lookup table will be needed for these in the future
        self.movement_ai: int = movement_ai
        self.target_ai: int = target_ai
        self.recover_ai: int = recover_ai
        self.retreat_ai: bool = retreat_ai #Will move in recovery mode or not
        self.x: int = x
        self.y: int = y
        self.width: int = width
        self.height: int = height
        give_square(self)
        self.read_klass_anim(None)        


    
    def read_klass_anim(self, klass):
        #This will be connected to the json database
        #For now it will create units on its own
        self.sprites = Spritesheet("resources/map_sprites/Mercenary-stand.png").load_strip((16,15,32,32), 5, -1)
        print(self.sprites)
        self.current_sprite = 0
        self.img = self.sprites[self.current_sprite]
        self.frame = 1

    
    def draw(self, display):
        display.blit(self.img, (self.rect.center[0]-16,self.rect.center[1]-17))
    
    def update(self):
        self.frame += 1

        if 1 <= self.frame <= 25:
            self.current_sprite = 0
        elif 26 <= self.frame <= 30:
            self.current_sprite = 2
        elif 31 <= self.frame <= 55:
            self.current_sprite = 4
        elif 56 <= self.frame <= 60:
            self.current_sprite = 2

        if self.frame >= 60:
            self.frame = 1
        
        self.img = self.sprites[int(self.current_sprite)]

    def move(self, x, y):
        pass

    def update_pos(self):
        self.abs_x = self.x * self.width
        self.abs_y = self.y * self.height
        self.pos = (self.x, self.y)
        self.abs_pos = (self.abs_x, self.abs_y)
        self.selected_unit = None
        self.rect.update(self.abs_x, self.abs_y, self.sqaure_size[0],self.sqaure_size[1])

    def __str__(self) -> str:
        return str(self.unit) + f"({self.x} , {self.y})"

    def __repr__(self) -> str:
        return str(self.unit) + f"({self.x} , {self.y})"