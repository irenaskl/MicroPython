
from machine import Pin, PWM
from time import sleep

pin = Pin(0, Pin.IN)  
led_pin = Pin(14, Pin.OUT)

pwm = PWM(led_pin, freq=5, duty=512)
pwm.deinit()