#!/usr/bin/env python

import math
import time
import psutil

from mote import Mote
from random import randint

print("""Process running - Pimoroni Mote - Fire mode
""")

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

def fire():
    for x in range(1,5):
        for y in range(16):
            z = randint(0,15)
            c = randint(0,7)
            if (c == 0 or c == 1 or c == 2 or c == 3):
                if c == 0:
		    mote.set_pixel(x,z,255,0,0,brightness=0.2)
                if c == 1:
		    mote.set_pixel(x,z,255,30,0,brightness=0.2)
                if c == 2:
		    mote.set_pixel(x,z,255,70,0,brightness=0.2)
                if c == 3:
		    mote.set_pixel(x,z,255,100,0,brightness=0.2)
            else:
		mote.set_pixel(x,z, 0, 0, 0)
        mote.show()
        time.sleep(randint(0,200)/1000.0)
                
try:
    while True:
        fire()

except KeyboardInterrupt:
	mote.clear()
	mote.show()
