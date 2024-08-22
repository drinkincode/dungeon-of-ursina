from ursina import *
class BaseStat(Entity):
    
    def __init__(self, name, statMax, color, position, scale=(0.5, 0.015), **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color,
            scale=scale,
            position=position,
            **kwargs
        )
        self.name = name
        self.stat_value = statMax
        self.statMax = statMax
        
    # return True if alive
    #   Fasle if dead
    def reduce_points(self, points):
        self.stat_value -= points
        if self.stat_value <= 0:
            return True
        return False
    
    def add_points(self, points):
        self.stat_value += points
        if self.stat_value > self.statMax:
            self.stat_value = self.statMax
            return True
        return False
    
    def print_stat(self):
        print(self.name + ': ' + str(self.stat_value))

    def update(self):
        self.scale_x = self.stat_value
    
    