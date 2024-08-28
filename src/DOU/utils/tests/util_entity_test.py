from ursina import *
from actors.player import Player
from utils.entity.top_corner_anchor import get_top_left_corner, top_left_to_center

window.borderless = False
app = Ursina()

window.color = color.light_gray
camera.orthographic = True
camera.fov = 20

# Example usage
inner_horizontal = Entity(model='cube', collider='box', color=color.red, scale=(5, 0.5, 1), position=(0, 6, 0))
top_left_corner = get_top_left_corner(inner_horizontal)
print(f"Top-left corner coordinates: {top_left_corner}")

center_coords = top_left_to_center(top_left_corner, inner_horizontal.scale)
print(f"Center coordinates: {center_coords}")

app.run()