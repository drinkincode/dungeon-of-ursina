from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Map
from actors.player import Player
from actors.npc import Npc


app = Ursina()
window.borderless = False
window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

# Define the map layout
map_1 = Map()

# Add interactive elements
player = Player(position=(-3, -2, 0))
player.stat_handler.stats_dict['health'].reduce_points(0.05)

npc = Npc()

app.run()
