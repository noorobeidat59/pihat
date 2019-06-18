#!/usr/bin/env python
from sense_hat import SenseHat

sense = SenseHat()
import random
import time
#sense.clear()
x = random.randint(0,7)
y= random.randint(0,7)
for loop in range(1,5):
	sense.set_pixel(x, y, (0, 255, 255))
	time.sleep(1)
	sense.set_pixel(x, y, (0, 0, 0))
	

