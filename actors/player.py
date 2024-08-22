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
        self.did_collide = False
        
        self.enabled_direction_dict = {'up': True, 'down': True, 'left': True, 'right': True}
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        self.movement()
        
    def movement(self):
        self.set_movement_controls('w', 's', 'a', 'd')
                 
    def set_movement_controls(self, up, down, left, right):
        if held_keys[up] and self.enabled_direction_dict['up']:
            if not self.check_collision(Vec3(0, time.dt * self.speed, 0)):
                self.y += time.dt * self.speed
            return
        elif held_keys[down] and self.enabled_direction_dict['down']:
            if not self.check_collision(Vec3(0, -time.dt * self.speed, 0)):
                self.y -= time.dt * self.speed
            return
        elif held_keys[left] and self.enabled_direction_dict['left']:
            if not self.check_collision(Vec3(-time.dt * self.speed, 0, 0)):
                self.x -= time.dt * self.speed
            return
        elif held_keys[right] and self.enabled_direction_dict['right']:
            if not self.check_collision(Vec3(time.dt * self.speed, 0, 0)):
                self.x += time.dt * self.speed
            return

    def check_collision(self, offset):
        original_position = self.position
        self.position += offset
        hit_info = self.intersects()
        self.position = original_position
        return hit_info.hit


