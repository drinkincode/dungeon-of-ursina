from ursina import *

def get_top_left_corner(entity: Entity) -> Vec3:
    # Calculate the top-left corner coordinates
    top_left_x = entity.x - (entity.scale_x / 2)
    top_left_y = entity.y + (entity.scale_y / 2)
    top_left_z = entity.z  # Assuming 2D plane, z-coordinate remains the same

    return Vec3(top_left_x, top_left_y, top_left_z)

def top_left_to_center(top_left, scale) -> Vec3:
    # Calculate the center coordinates from the top-left corner coordinates and scale
    center_x = top_left.x + (scale[0] / 2)
    center_y = top_left.y - (scale[1] / 2)
    center_z = top_left.z  # Assuming 2D plane, z-coordinate remains the same

    return Vec3(center_x, center_y, center_z)
