import random

from mutateshape.utils import get_current_obj, get_camera, get_wall


def on_loop():
    road = get_current_obj()
    cam = get_camera()

    if cam.worldPosition.y > road.worldPosition.y:
        road.worldPosition.y += 280.0
        if random.random() < 0.2: # TODO: play with it
            move_wall(road, cam)


def move_wall(road, cam):
    wall = get_wall()
    if cam.worldPosition.y > wall.worldPosition.y:
        wall.worldPosition.z = 0
        wall.worldPosition.y = road.worldPosition.y
