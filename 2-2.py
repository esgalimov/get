import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)


number1 = [1 for i in range(8)]
number2 = [0, 1, 1, 1, 1, 1, 1, 1]
number3 = [0, 1, 0, 0, 0, 0, 0, 0]
number4 = [0, 0, 1, 0, 0, 0, 0, 0]
number5 = [0, 0, 0, 0, 0, 1, 0, 1]
number6 = [0 for i in range(8)]

GPIO.output(dac, number5)

time.sleep(10)

GPIO.output(dac, 0)

GPIO.cleanup()


x = [255, 127, 64, 32, 5, 0, 256]
y = [3.27, 1.63, 0.82, 0.50, 0.48, 0.48, 0.48]

fig, ax = plt.subplots(figsize=(10, 8))

ax.plot(x, y)

plt.show()