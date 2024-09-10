from ursina import *
from DoU.actors.wall import Wall

class Map():
    def __init__(self, map_id = 0):
        if map_id == 0:
            self.border_walls = create_walls()
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
        else:
            self.create_map(map_id)
    def create_map(self, map_id):
        if map_id == 1:
            self.border_walls = create_walls()
            self.interior_walls = []
            self.interior_walls.append(
                Wall(name='inner_vertical', color=color.gray, scale=(0.5, 12, 1), position=(0, -1.5, 0))
            )
            self.interior_walls.append(
                Wall(name='inner_horizontal', color=color.gray, scale=(5, 0.5, 1), position=(0, 6, 0))
            )
            self.interior_walls.append(
                Wall(name='inner_horizontal2', color=color.gray, scale=(12, 0.5, 1), position=(11.5, 6, 0))
            )
        

def create_walls(
    walls_scale_pos_list=[
        [(35, 0.5, 1), (0, 9, 0), color.gray],
        [(35, 0.5, 1), (0, -9, 0), color.gray],
        [(0.5, 18.5, 1), (-17.5, 0, 0), color.gray], 
        [(0.5, 18.5, 1), (17.5, 0, 0), color.gray]
    ]
):
    wall_dict = {}
    name_list = ['lower_border_wall', 'upper_border_wall', 'left_border_wall', 'right_border_wall']
    for i in range(len(walls_scale_pos_list)):
        name = name_list[i]
        scale = walls_scale_pos_list[i][0]
        pos = walls_scale_pos_list[i][1]
        color = walls_scale_pos_list[i][2]
        
        wall_dict[name] = Wall(name=name, scale=scale, position=pos, color=color)
    return wall_dict