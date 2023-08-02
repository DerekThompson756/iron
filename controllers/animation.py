from abc import ABC, abstractmethod

class Animation(ABC):
    def __init__(self):
        self.img_path = str
        self.sprites = []
        self.current_sprite = int
        self.img = None
        self.frame = int

    @abstractmethod
    def draw(self, display):
        pass

    @abstractmethod
    def update(self):
        pass
    