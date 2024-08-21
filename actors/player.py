from ursina import *

class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'quad'
        self.texture = 'player_sprite'
        self.scale_y = 4
        self.scale_x = 2.33
        self.collider = 'box'
        self.speed = 5

        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.movement()

    def movement(self):
        self.set_movement_controls('w', 's', 'a', 'd')
        
                 
    def set_movement_controls(self, up, down, left, right):
        if held_keys[up]:
            self.y += time.dt * self.speed
        if held_keys[down]:
            self.y -= time.dt * self.speed
        if held_keys[left]:
            self.x -= time.dt * self.speed
        if held_keys[right]:
            self.x += time.dt * self.speed


