from ursina import *
from stats.baseStat import BaseStat
from stats.baseStatHandler import BaseStatHandler
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.model = 'quad'
        self.texture = 'player_sprite_cropped'
        self.scale_y = 2
        self.scale_x = 2
        self.collider = 'box'
        self.speed = 5
        self.jump_height = 0.3
        self.gravity = 1
        self.vertical_velocity = 0
        self.grounded = False
        self.enabled_direction_dict = {'up': True, 'down': True, 'left': True, 'right': True}
        self.init_stat_list = [
            ['health', 100],
            ['stamina', 100],
            ['mana', 100]
        ] 
        self.stat_handler = BaseStatHandler(self.init_stat_list)
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.movement()

    def movement(self):
        if held_keys['w'] and self.enabled_direction_dict['up']:
            if not self.check_collision(Vec3(0, time.dt * self.speed, 0)):
                self.y += time.dt * self.speed
        if held_keys['s'] and self.enabled_direction_dict['down']:
            if not self.check_collision(Vec3(0, -time.dt * self.speed, 0)):
                self.y -= time.dt * self.speed
        if held_keys['a'] and self.enabled_direction_dict['left']:
            if not self.check_collision(Vec3(-time.dt * self.speed, 0, 0)):
                self.x -= time.dt * self.speed
        if held_keys['d'] and self.enabled_direction_dict['right']:
            if not self.check_collision(Vec3(time.dt * self.speed, 0, 0)):
                self.x += time.dt * self.speed

    def check_collision(self, offset):
        original_position = self.position
        self.position += offset
        hit_info = self.intersects()
        self.position = original_position
        return hit_info.hit
