import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

def adc():
    for lvl in range(max_lvl):
        GPIO.output(dac, dec2bin(lvl))
        time.sleep(delta_t)
        if GPIO.input(comp) == 0:
            return lvl

def voltage(lvl):
    return round((lvl / max_lvl) * max_volt, 2)

delta_t = 0.0007
max_lvl = 256
max_volt = 3.3

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        value = adc()
        print(f"level = {value}, V = {voltage(value)}")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()