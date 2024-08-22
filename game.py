from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from maps.map import Room, Map

class Game(Ursina):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup()

    def setup(self):
        window.color = color.light_gray
        camera.orthographic = True
        camera.fov = 20

        # Define the map layout
        self.room1 = Room(position=(0, 0), scale=(4, 3), label="Loot")
        self.room2 = Room(position=(5, 0), scale=(3, 3), label="Level Exit")
        self.room3 = Room(position=(0, -4), scale=(3, 3), label="Loot")
        self.room4 = Room(position=(-5, 0), scale=(3, 3), label="Loot")

        # Add border walls
        self.map_1 = Map()

        # Add interactive elements
        self.loot1 = Entity(model='sphere', color=color.gold, scale=0.5, position=(0.5, -0.5, 0), parent=self.room1)
        self.loot2 = Entity(model='sphere', color=color.gold, scale=0.5, position=(-0.5, -0.5, 0), parent=self.room3)

        # Create the player entity
        self.player = Entity(model='quad', color=color.blue, scale=(1, 1), collider='box')
        self.player.position = (0, 0)

    def update(self):
        # Debug prints to check if keys are being detected
        if held_keys['d']:
            print("Moving right")
            self.player.x += time.dt * 5
        if held_keys['a']:
            print("Moving left")
            self.player.x -= time.dt * 5
        if held_keys['w']:
            print("Moving up")
            self.player.y += time.dt * 5
        if held_keys['s']:
            print("Moving down")
            self.player.y -= time.dt * 5

