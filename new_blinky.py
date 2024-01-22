import time
import board
import neopixel

# Calls the circuit Python neopixel library, specifies the default board 
# pins for the Neopixels, and the number of neopixels to access.  Returns a 
# list 'pixels' of indexable neopixles
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)

while True:
    pixels.fill((180, 220, 30))
    time.sleep(0.8)
    pixels.fill((110, 25, 200))
    time.sleep(0.5)
