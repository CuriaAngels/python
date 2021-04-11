import time
from random import randint
from rpi_ws281x import *
 
# LED strip configuration:
LED_COUNT      = 270      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN       = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 120      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def fullstrip(strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()
        
def fire(strip):
#    for i in range(0,44):
#        strip.setPixelColor(i, Color(0, 255, 0))
#    for i in range(45,145):
#        strip.setPixelColor(i, Color(255, 255, 0))
#    for i in range(146,182):
#        strip.setPixelColor(i, Color(0, 255, 0))
#    for i in range(183,215):
#        strip.setPixelColor(i, Color(255, 255, 0))
#    for i in range(216,243):
#        strip.setPixelColor(i, Color(0, 255, 0))
#    for i in range(244,270):
#        strip.setPixelColor(i, Color(255, 255, 0))
#    strip.show()            
#    time.sleep(60)
    for i in range(0,44):
        strip.setPixelColor(i, Color(75, 0, 130))
    for i in range(45,145):
        strip.setPixelColor(i, Color(100,100, 0))
    for i in range(146,182):
        strip.setPixelColor(i, Color(75, 0, 130))
    for i in range(183,215):
        strip.setPixelColor(i, Color(100,100, 0))
    for i in range(216,243):
        strip.setPixelColor(i, Color(75, 0, 130))
    for i in range(244,270):
        strip.setPixelColor(i, Color(100,100, 0))
    strip.show()            
    time.sleep(60)

# Main program logic follows:
if __name__ == '__main__':
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()
 
    print ('Press Ctrl-C to quit.')
 
    try:
 
        while True:
            fire(strip)
 
    except KeyboardInterrupt:
            fullstrip(strip, Color(0,0,0))
