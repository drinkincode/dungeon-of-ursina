from ursina import *

class Map():
    def __init__(self):
        self.border_walls = BorderWalls()
        self.interior_walls = []
        self.interior_walls.append(
            Wall(name='inner_vertical', color=color.gray, scale=(0.5, 15, 1), position=(0, -1.5, 0))
        )
        self.interior_walls.append(
            Wall(name='inner_horizontal', color=color.gray, scale=(5, 0.5, 1), position=(0, 6, 0))
        )
        self.interior_walls.append(
            Wall(name='inner_horizontal2', color=color.gray, scale=(12, 0.5, 1), position=(11.5, 6, 0))
        )
    
    
class BorderWalls(Entity):
    def __init__(self, walls_scale_pos_list: list = 
            [
                [(35, 0.5, 1), (0, -9, 0), color.gray], 
                [(35, 0.5, 1), (0, 9, 0), color.gray],
                [(0.5, 18.5, 1), (-17.5, 0, 0), color.gray], 
                [(0.5, 18.5, 1), (17.5, 0, 0), color.gray]
            ]
        ):
        self.wall_dict = {}
        self.name_list = ['lower_border_wall', 'upper_border_wall', 'left_border_wall', 'right_border_wall']
        for i in range(len(walls_scale_pos_list)):
            name = self.name_list[i]
            scale = walls_scale_pos_list[i][0]
            pos = walls_scale_pos_list[i][1]
            color = walls_scale_pos_list[i][2]
            
            self.wall_dict[name] = Wall(name=name, scale=scale, position=pos, color=color)
        
class Wall(Entity):
    def __init__(self, name: str, scale: tuple, position: tuple, color: color):
        
        super().__init__(
            model='cube', 
            collider = 'box', 
            color=color, 
            scale=scale, 
            position=position
        )
        self.name = name