from ursina import *
from stats.baseStat import BaseStat
from stats.baseStatHandler import BaseStatHandler
class Actor(Entity):
    def __init__(
            self, 
            name,
            texture='player_sprite_cropped', 
            scale=(2, 2), 
            speed=5, 
            enabled_direction_dict={'up': True, 'down': True, 'left': True, 'right': True}, 
            init_stat_list=[
                ['health', 0.15, color.red, (0, -0.05), False]
            ],
            position = (0, 0, 0)
        ):
        super().__init__()
        self.model = 'quad'
        self.texture = texture
        self.scale = scale
        self.collider = 'box'
        self.speed = speed
        self.enabled_direction_dict = enabled_direction_dict
        self.name = name
        self.position = position
        # stat: name, stat_max, color, position
        self.stat_handler = BaseStatHandler(init_stat_list)
