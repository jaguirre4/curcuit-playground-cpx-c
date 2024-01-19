import time
from adafruit_circuitplayground import cp

while True:
    cp.red_led = True
    time.sleep(0.8)
    cp.red_led = False
    time.sleep(0.8)
