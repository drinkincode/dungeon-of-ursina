from ursina import *


class Room(Entity):
    def __init__(self, position=(0,0,0), scale=(2,2), label=None, **kwargs):
        super().__init__(
            model='quad',
            color=color.light_gray,
            position=position,
            scale=scale,
            origin=(-0.5, 0.5),
            **kwargs
        )
        # Add a label to the room
        if label:
            self.text = Text(
                text=label, 
                parent=self, 
                scale=2, 
                origin=(-0.5, -0.5),
                position=(0.5, -0.5)
            )

class Map():
    def __init__(self):
        self.walls()
        inner_vertical = Entity(model='cube', color=color.gray, scale=(0.5, 15, 1), position=(0, -1.5, 0))
        inner_horizontal = Entity(model='cube', color=color.gray, scale=(5, 0.5, 1), position=(0, 6, 0))
        inner_horizontal2 = Entity(model='cube', color=color.gray, scale=(12, 0.5, 1), position=(11.5, 6, 0))
    
        
    def walls(self):
        # Boarder Walls
        lower_wall = Entity(model='cube', color=color.gray, scale=(35, 0.5, 1), position=(0, -9, 0))  # floor 
        upper_wall = Entity(model='cube', color=color.gray, scale=(35, 0.5, 1), position=(0, 9, 0))  # ceilling
        left_wall = Entity(model='cube', color=color.gray, scale=(0.5, 18.5, 1), position=(-17.5, 0, 0))  # left
        right_wall = Entity(model='cube', color=color.gray, scale=(0.5, 18.5, 1), position=(17.5, 0, 0))  # right