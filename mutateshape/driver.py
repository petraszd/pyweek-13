import bge
from mathutils import Vector

from mutateshape.utils import get_current_obj


MAX_SIDE_DELTA = 9.3
MAX_SPEED_INIT = 100.0


def on_init():
    driver = get_current_obj()
    driver['max_speed'] = MAX_SPEED_INIT


def on_loop():
    driver = get_current_obj()
    t = get_t(driver)

    if driver['is_forward']:
        increase_speed(driver, t)
    else:
        decrease_speed(driver, t)

    if driver['speed']:
        driver.worldPosition += get_direction(driver) * driver['speed'] * t

    normalize_side_position(driver)

    # TODO: increase max_speed on intervals

    driver['prev_time'] = driver['timer']


def normalize_side_position(driver):
    if driver.worldPosition.x > 0.0:
        driver.worldPosition.x = min(driver.worldPosition.x, MAX_SIDE_DELTA)
    else:
        driver.worldPosition.x = max(driver.worldPosition.x, -MAX_SIDE_DELTA)


def get_direction(driver):
    direction = Vector((0.0, 1.0, 0.0))
    if driver['is_left'] and not is_on_left_edge(driver):
        direction += Vector((-1.0, 0.0, 0.0))
    if driver['is_right'] and not is_on_right_edge(driver):
        direction += Vector((1.0, 0.0, 0.0))
    direction.normalize()
    return direction


def is_on_right_edge(driver):
    return driver.worldPosition.x >= MAX_SIDE_DELTA


def is_on_left_edge(driver):
    return driver.worldPosition.x <= -MAX_SIDE_DELTA


def get_t(driver):
    return driver['timer'] - driver['prev_time']


def increase_speed(driver, t):
    # TODO: play with various ways to inc/dec speed
    driver['speed'] = min(driver['max_speed'],
                          driver['speed'] + t * driver['max_speed'])

def decrease_speed(driver, t):
    driver['speed'] = max(0.0, driver['speed'] - t * driver['max_speed'])


def on_collision():
    print(bge.logic.getSceneList())
    bge.logic.addScene('Lose')
    print("COLLISION") # TODO: change scenes


def on_key():
    co = bge.logic.getCurrentController()
    sensor = co.sensors["Keyboard"]

    for key,status in sensor.events:
        if status == bge.logic.KX_INPUT_JUST_ACTIVATED:
            if key == bge.events.WKEY:
                on_forward_on()
            elif key == bge.events.SKEY:
                on_backard_on()
            elif key == bge.events.AKEY:
                on_left_on()
            elif key == bge.events.DKEY:
                on_right_on()
        elif status == bge.logic.KX_INPUT_JUST_RELEASED:
            if key == bge.events.WKEY:
                on_forward_off()
            elif key == bge.events.SKEY:
                on_backard_off()
            elif key == bge.events.AKEY:
                on_left_off()
            elif key == bge.events.DKEY:
                on_right_off()


def on_forward_on():
    get_current_obj()['is_forward'] = True


def on_forward_off():
    get_current_obj()['is_forward'] = False


def on_backard_on():
    get_current_obj()['is_backward'] = True


def on_backard_off():
    get_current_obj()['is_backward'] = False


def on_left_on():
    get_current_obj()['is_left'] = True


def on_left_off():
    get_current_obj()['is_left'] = False


def on_right_on():
    get_current_obj()['is_right'] = True


def on_right_off():
    get_current_obj()['is_right'] = False
