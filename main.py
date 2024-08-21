import time
# t = time.time()

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Room, Map
from actors.player import Player
# window.vsync = False
window.borderless = False
app = Ursina()

window.color = color.light_gray
camera.orthographic = True
camera.fov = 20
# ground = Entity(model='cube', color=color.olive.tint(-.4), z=-.1, y=-1, origin_y=.5, scale=(1000,100,10), collider='box', ignore=True)

# create_map(5)

# Define the map layout


# Boarder Walls
map_1 = Map()

# Add interactive elements
player = Player(position=(-3, -2, 0))


app.run()
