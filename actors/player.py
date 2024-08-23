from ursina import *
from stats.baseStat import BaseStat
from stats.baseStatHandler import BaseStatHandler
from actors.actor import Actor
class Player(Actor):
    def __init__(self, position=(-3, -2, 0)):
        self.texture = 'player_sprite_cropped'
        self.enabled_direction_dict = {'up': True, 'down': True, 'left': True, 'right': True}
        name = 'player'
        self.init_stat_list = [
            ['health', 0.15, color.red, (0, -0.05), True],
            ['stamina', 0.15, color.green, (0, 0), True],
            ['mana', 0.15, color.blue, (0, 0.05), True]
        ]
        super().__init__(
            name=name,
            texture=self.texture, 
            enabled_direction_dict=self.enabled_direction_dict, 
            init_stat_list=self.init_stat_list,
            position=position
        )

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
