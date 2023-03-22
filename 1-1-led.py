import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(23, GPIO.IN)

while True:
    if GPIO.input(23) == 1:
        GPIO.output(14, 1)
    else:
        GPIO.output(14, 0)

