import bge


def get_current_obj():
    return bge.logic.getCurrentController().owner


def get_camera():
    return bge.logic.getCurrentScene().active_camera


def get_wall():
    scene = bge.logic.getCurrentScene()
    wall = scene.objects['Wall']
    return wall
