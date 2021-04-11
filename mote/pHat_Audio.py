#!/usr/bin/env python

import math
import time
import sys

sys.path.append('../python/')

import speakerphat


speed = 4

try:
    while True:
        offset = int((math.sin(time.time() * speed) * 5) + 5)

        speakerphat.clear()
        speakerphat.set_led(offset,255)
        speakerphat.show()

except KeyboardInterrupt:
	speakerphat.clear()
	speakerphat.show()        
