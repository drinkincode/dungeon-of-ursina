from ursina import *
from actors.player import Player
# Assuming player is already defined elsewhere and has a basestathandler attribute
# from player_module import player  # Example import if player is defined in another module

# Create stat bars

class StatBar(Entity):
    def __init__(self, stat_name, color, position, scale=(0.5, 0.05), **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color,
            scale=scale,
            position=position,
            **kwargs
        )
        self.stat_value = 0.5
        self.stat_name = stat_name

    def update(self):
        self.scale_x = self.stat_value
        
# health_bar = StatBar(parent=camera.ui, model='quad', color=color.red, scale=(0.5, 0.05), position=(-0.5, 0.4))
# stamina_bar = StatBar(parent=camera.ui, model='quad', color=color.green, scale=(0.5, 0.05), position=(-0.5, 0.35))
