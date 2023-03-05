from neopixel import NeoPixel
from machine import Pin, PWM
from time import sleep

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 8)
for i in range(8):
    np[i] = (i*2, 0, (7-i)*2)
    sleep(1/2)
    np.write()
