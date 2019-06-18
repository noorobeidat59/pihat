#!/usr/bin/env python
from sense_hat import SenseHat

sense = SenseHat()


red = (255, 0, 0)
blue = (0, 0, 255)

speed = 0.07
message = "Barcalona!"

sense.show_message(message, speed, text_colour=red, back_colour=blue)

sense.clear()
