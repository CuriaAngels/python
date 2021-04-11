import time
from random import randint
from rpi_ws281x import *
 
# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN       = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def fullstrip(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        
def fire(strip):
    for i in range(strip.numPixels()):
        x = randint(0,strip.numPixels()-1)
        y = randint(0,7)
        if (y == 0 or y == 1 or y == 2 or y == 3):
            if y == 0:
                strip.setPixelColor(x, Color(255, 0, 0))
            if y == 1:
                strip.setPixelColor(x, Color(255, 30, 0))
            if y == 2:
                strip.setPixelColor(x, Color(255, 70, 0))
            if y == 3:
                strip.setPixelColor(x, Color(255, 100, 0))
        else:
            strip.setPixelColor(x, Color(0, 0, 0))
        strip.show()
        time.sleep(randint(0,200)/1000.0)
                
 
# Main program logic follows:
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
 
    try:
 
        while True:
            fullstrip(strip, Color(255,255,255))
 
    except KeyboardInterrupt:
            fullstrip(strip, Color(0,0,0))
