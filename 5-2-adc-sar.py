import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def adc():
    ret = 0
    for i in range(7, -1, -1):
        ret += 2 ** i
        GPIO.output(dac, dec2bin(ret))
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            ret -= 2 ** i
    return ret


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