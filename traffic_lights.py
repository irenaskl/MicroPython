from neopixel import NeoPixel
from machine import Pin, PWM
from time import sleep

pin = Pin(2, Pin.OUT)
np = NeoPixel(pin, 8)
for i in range(8):
    if i == 0 or i == 1:
        np[i] = (255, 0, 0)
        sleep(0)
        np.write()
    elif i == 2 or i == 3:
        np[i] = (255, 100, 0)
        sleep(1)
        np.write()
    else:
        np[i] = (0, 255, 0)
        sleep(1)
        np.write()

for i in range(8):
    np[i] = (0, 0, 0)
sleep(5)
np.write()
