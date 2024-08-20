import time
# t = time.time()

from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Room, Map

# window.vsync = False
window.borderless = False
app = Ursina()

window.color = color.light_gray
camera.orthographic = True
camera.fov = 20
# ground = Entity(model='cube', color=color.olive.tint(-.4), z=-.1, y=-1, origin_y=.5, scale=(1000,100,10), collider='box', ignore=True)

# create_map(5)

# Define the map layout
room1 = Room(position=(0, 0), scale=(4, 3), label="Loot")
room2 = Room(position=(5, 0), scale=(3, 3), label="Level Exit")
room3 = Room(position=(0, -4), scale=(3, 3), label="Loot")
room4 = Room(position=(-5, 0), scale=(3, 3), label="Loot")

# Boarder Walls
map_1 = Map()

# Add interactive elements
loot1 = Entity(model='sphere', color=color.gold, scale=0.5, position=(0.5, -0.5, 0), parent=room1)
loot2 = Entity(model='sphere', color=color.gold, scale=0.5, position=(-0.5, -0.5, 0), parent=room3)

player = PlatformerController2d(gravity=0)
player.x=1
player.y = raycast(player.world_position, player.down).world_point[1] + .01
# camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))

input_handler.bind('right arrow', 'a')
input_handler.bind('left arrow', 'd')
input_handler.bind('up arrow', 'w')
input_handler.bind('down arrow', 's')


app.run()
