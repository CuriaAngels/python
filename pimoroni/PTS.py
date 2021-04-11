#!/usr/bin/env python
import time

from mote import Mote

print("""Praise the Sun

Press Ctrl+C to exit.
""")

mote = Mote()

mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


def show_graph1():
    mote.clear()
    for x in range(16):
        if (x % 2) == 0: 
            mote.set_pixel(1,x, 255, 147, 41)
            mote.set_pixel(2,x, 255, 147, 41)
            mote.set_pixel(3,x, 255, 147, 41)
            mote.set_pixel(4,x, 255, 147, 41)
        else:
            mote.set_pixel(1,x, 0, 0, 0)
            mote.set_pixel(2,x, 0, 0, 0)
            mote.set_pixel(3,x, 0, 0, 0)
            mote.set_pixel(4,x, 0, 0, 0)
    mote.show()

def show_graph2():
    mote.clear()
    for x in range(16):
        if (x % 2) == 0: 
            mote.set_pixel(1,x, 0, 0, 0)
            mote.set_pixel(2,x, 0, 0, 0)
            mote.set_pixel(3,x, 0, 0, 0)
            mote.set_pixel(4,x, 0, 0, 0)
        else:
            mote.set_pixel(1,x, 255, 255, 255)
            mote.set_pixel(2,x, 255, 255, 255)
            mote.set_pixel(3,x, 255, 255, 255)
            mote.set_pixel(4,x, 255, 255, 255)
    mote.show()

try:
    while True:
        show_graph1()
	time.sleep(2)
        show_graph2()
	time.sleep(2)

except KeyboardInterrupt:
	mote.clear()
	mote.show()
