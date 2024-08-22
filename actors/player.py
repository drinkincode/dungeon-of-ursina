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
        self.current_direction = 'up'
        
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self):
        current_direction = self.current_direction
        if self.check_collision():
            self.enabled_direction_dict[self.current_direction] = False
        self.movement()
        self.enabled_direction_dict[current_direction] = True
        
    def movement(self):
        self.set_movement_controls('w', 's', 'a', 'd')
        
                 
    def set_movement_controls(self, up, down, left, right):
        if held_keys[up] and self.enabled_direction_dict['up']:
            self.current_direction = 'up'
            self.y += time.dt * self.speed
            return
        elif held_keys[down] and self.enabled_direction_dict['down']:
            self.current_direction = 'down'
            self.y -= time.dt * self.speed
            return
        elif held_keys[left] and self.enabled_direction_dict['left']:
            self.current_direction = 'left'
            self.x -= time.dt * self.speed
            return
        elif held_keys[right] and self.enabled_direction_dict['right']:
            self.current_direction = 'right'
            self.x += time.dt * self.speed
            return

    def check_collision(self):
        hit_info = self.intersects()
        if hit_info.hit:
            print(f'Collision with {hit_info.entity}')
            print(hit_info.world_point)
            print(hit_info.world_point)
            return True


