from ursina import *
from actors.actor import Actor

class Wall(Actor):
    def __init__(self, name: str, scale: tuple, position: tuple, color: color):
        
        super().__init__(
            model='cube',
            scale=scale, 
            position=position,
            name=name
        )
        self.color = color