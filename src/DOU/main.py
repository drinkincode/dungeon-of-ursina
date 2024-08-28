from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Map
from actors.actor import Actor
from actors.player import Player
from actors.npc import Npc
from menus.pause_menu import PauseMenu

app = Ursina()
window.borderless = False
window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

pause_menu = PauseMenu()

def input(key):
        if key == 'escape':
            pause_menu.enabled = not pause_menu.enabled
            pause_menu.toggle_pause()


# Define the map layout
map_1 = Map()

# Add interactive elements
player = Player(position=(-3, -2, 0))
player.stat_handler.stats_dict['health'].reduce_points(0.05)


# [
#     {
#         'atkName': 'punch',
#         'atkDamage': 10,
#         'atkLevel': 1,
#         'atkCost': []
#     }
# ]
npc = Npc()

app.run()
