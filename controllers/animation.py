from abc import ABC, abstractmethod
from app.data.klass import Klass

class Animation(ABC):
    def __init__(self):
        self.img_path = str
        self.sprites = []
        self.current_sprite = int
        self.img = None
        self.frame = int


    def read_klass_anim(self, Klass):
        pass

    def slice_spritesheet(self, img_path):
        pass


    def draw(self, display):
        pass

    def update(self):
        pass
    