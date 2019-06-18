#!/usr/bin/env python
from sense_hat import SenseHat

sense = SenseHat()
import time
import random 
r = random.randint(0,255)
sense.show_letter("N" , (r, 0, 0))
time.sleep(1)
sense.show_letter("O" , (0, r, 0))
time.sleep(1)
sense.show_letter("!" , (0, 0, r))
time.sleep(1)
sense.clear()
