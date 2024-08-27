from ursina import *
from stats.baseStat import BaseStat
from stats.baseStatHandler import BaseStatHandler
from actors.actor import Actor
from ursina import Vec3

class Npc(Actor):
    def __init__(
            self, 
            position=(-4, 0, 0), 
            texture = 'player_sprite_cropped', 
            enabled_direction_dict = {'up': True, 'down': True, 'left': True, 'right': True}, 
            name='npc', 
            speed=2
        ):
        
        self.texture = texture
        self.enabled_direction_dict = enabled_direction_dict
        name = 'npc'
        speed = speed
        self.init_stat_list = [
            ['health', 0.15, color.red, (0, -0.05), False],
            ['stamina', 0.15, color.green, (0, 0), False],
            ['mana', 0.15, color.blue, (0, 0.05), False]
        ]
        
        super().__init__(
            name=name,
            texture=self.texture, 
            enabled_direction_dict=self.enabled_direction_dict, 
            init_stat_list=self.init_stat_list,
            position=position,
            speed=speed
        )

    def update(self):
        self.movement()

    def movement(self):
        # Define possible movement directions
        directions = [
            Vec3((time.dt * self.speed), 0, 0),  # Right
            Vec3(-(time.dt * self.speed), 0, 0), # Left
            Vec3(0, (time.dt * self.speed), 0),  # Up
            Vec3(0, -(time.dt * self.speed), 0)  # Down
        ]
        
        # Choose a random direction
        # direction = random.choice(directions)
        direction = directions[2]
        
        # Check for collision
        if not self.check_collision(direction):
            # Update position if no collision
            self.position += direction

    def check_collision(self, offset):
        original_position = self.position
        self.position += offset
        hit_info = self.intersects()
        self.position = original_position
        return hit_info.hit