from TrafficLight import TrafficLight
from sense_hat import SenseHat
import time

R = [True, False, False]
A = [False, True, False]
G = [False, False, True]


def one_light():
    s = SenseHat()
    s.low_light = True
    s.clear()

    light_1 = TrafficLight(sensehat=s, location=(0, 0))
    light_2 = TrafficLight(sensehat=s, location=(3, 0))
    light_3 = TrafficLight(sensehat=s, location=(6, 0))

    sequence_a = [
        [G, R, G, 5],
        [A, R, A, 1],
        [R, R, R, 2],
    ]
    sequence_b = [
        [R, G, R, 5],
        [R, A, R, 1],
        [R, R, R, 2]
    ]

    for lights in sequence_a:
        light_1.change_state(lights[0])
        light_2.change_state(lights[1])
        light_3.change_state(lights[2])
        time.sleep(lights[3])
    # Check for a pedestrian button press
    for lights in sequence_b:
        light_1.change_state(lights[0])
        light_2.change_state(lights[1])
        light_3.change_state(lights[2])
        time.sleep(lights[3])
    # Check for a pedestrian button press


# Press the green button in the gutter to run the script.
one_light()
