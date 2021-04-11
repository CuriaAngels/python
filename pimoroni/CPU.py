#!/usr/bin/env python

import math
import time
import psutil

from mote import Mote

print("""CPU

Press Ctrl+C to exit.
""")

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)

def show_graph(v, r, g, b):
    v *= 8
    for x in range(16):
        if v  < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v,1.0) * c) for c in [r,g,b]]
        mote.set_pixel(1,x, r, g, b)
        mote.set_pixel(2,x, r, g, b)
        mote.set_pixel(3,x, r, g, b)
        mote.set_pixel(4,x, r, g, b)
        mote.set_pixel(1,15, 255, 0, 0)
        mote.set_pixel(2,15, 255, 0, 0)
        mote.set_pixel(3,15, 255, 0, 0)
        mote.set_pixel(4,15, 255, 0, 0)
        
        v -= 1
    mote.show()


try:
    while True:
        v = psutil.cpu_percent() / 100.0
        show_graph(v, 255, 0, 0)
        #print(v)
        time.sleep(0.10)

except KeyboardInterrupt:
	mote.clear()
	mote.show()
