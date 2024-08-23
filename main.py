import time
# t = time.time()

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Map
from actors.player import Player

from menus.stat_menu import StatBar
# window.vsync = False
window.borderless = False
app = Ursina()

window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

# create_map(5)

# Define the map layout

# Boarder Walls
map_1 = Map()
# stat_bar = StatBar(stat_name='health', color=color.green, position=(-0.5, 0.35))

# Add interactive elements
player = Player(position=(-3, -2, 0))
player.stat_handler.stats_dict['health'].reduce_points(0.05)
app.run()
