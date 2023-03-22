import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    t = int(input())
except ValueError:
    t = 10

try:
    num = 0
    delta = 1

    while True:
        GPIO.output(dac, dec2bin(num))
        time.sleep(t / 512)
        if (num + delta) > 255 or (num + delta) < 0:
            delta = -delta
        num += delta

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()