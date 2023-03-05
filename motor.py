#hnedy GND
#cerveny 3V3
#oranzovy D4

from machine import Pin, PWM
from time import sleep

pin = Pin(2, Pin.OUT)
pwm = PWM(pin, freq=50, duty=77)


sleep(1)
pwm.duty(120)
