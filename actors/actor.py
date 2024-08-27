from ursina import *
from stats.baseStat import BaseStat
from stats.baseStatHandler import BaseStatHandler
class Actor(Entity):
    def __init__(
            self, 
            name,
            texture=None,
            scale=(2, 2), 
            speed=5, 
            enabled_direction_dict=None, 
            init_stat_list=[],
            position = (0, 0, 0),
            model = 'quad',
            collider = 'box',
            update = None,
        ):
        super().__init__()
        self.model = model
        self.texture = texture
        self.scale = scale
        self.collider = collider
        self.speed = speed
        self.enabled_direction_dict = enabled_direction_dict
        self.name = name
        self.position = position
        # stat: name, stat_max, color, position
        self.stat_handler = BaseStatHandler(init_stat_list)
        self.original_update = update
