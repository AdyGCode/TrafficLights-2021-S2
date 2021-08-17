# ---------------------------------------------------------------------
# Filename      : TrafficLight.py
# Location      : ./
# Project       : TrafficLights
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 17/8/21
# Version       : 0.1
# Description   :
#   The Traffic Light class that handles the state of the lights.
#
#   Uses the Light class which handles the colour, location and
#   state of a single light in the traffic light group.
#
# ---------------------------------------------------------------------
from sense_hat import SenseHat
import time


class Light:
    """Light - a single light status class
    """

    def __init__(self, sensehat=None, colour=(0, 0, 0), state=False, location=(0, 0)):
        """
        Set up a light to have a colour, status and location

        :param colour: The colour of the light, RGB tuple (R,G,B)
        :param state: True/False (On/Off)
        :param location: Position on the grid for the light
        """
        self.sensehat = sensehat
        self.colour = colour
        self.state = state
        self.location = location

    def draw(self):
        """
        Draw the light on the display
        :return:
        """
        pixels = [(0, 0), (0, 1), (1, 1), (1, 0)]
        for pixel in pixels:
            self.sensehat.set_pixel(self.location[0] + pixel[0], self.location[1] + pixel[1], (0, 0, 0))
        if self.state:
            for pixel in pixels:
                self.sensehat.set_pixel(self.location[0] + pixel[0], self.location[1] + pixel[1], self.colour)


class TrafficLight:
    def __init__(self, sensehat=None, location=(0, 0)):
        xpos = location[0]
        ypos = location[1]
        self.red = Light(sensehat, colour=(255, 0, 0), state=True, location=(xpos, ypos))
        self.yellow = Light(sensehat, colour=(255, 255, 0), state=False, location=(xpos, ypos + 2))
        self.green = Light(sensehat, colour=(0, 255, 0), state=False, location=(xpos, ypos + 4))

    def change_state(self, pattern=None):
        if pattern is None:
            pattern = [False, False, False]
        self.red.state = pattern[0]
        self.yellow.state = pattern[1]
        self.green.state = pattern[2]
        self.draw()

    def draw(self):
        self.red.draw()
        self.yellow.draw()
        self.green.draw()



class PedestrianLight:
    def __init__(self, sensehat=None, location=(0, 0)):
        xpos = location[0]
        ypos = location[1]
        self.red = Light(sensehat, colour=(255, 0, 0), state=True, location=(xpos, ypos))
        self.green = Light(sensehat, colour=(0, 255, 0), state=False, location=(xpos, ypos + 4))

    def change_state(self, pattern=None):
        if pattern is None:
            pattern = [False, False, False]
        self.red.state = pattern[0]
        self.green.state = pattern[2]
        self.draw()

    def draw(self):
        self.red.draw()
        self.green.draw()
