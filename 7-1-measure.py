import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time


def dec2bin(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def adc():
    ret = 0
    for i in range(7, -1, -1):
        ret += 2 ** i
        GPIO.output(dac, dec2bin(ret))
        time.sleep(delta_t)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            ret -= 2 ** i
    return ret


def voltage(lvl):
    return round((lvl / max_lvl) * max_volt, 2)

delta_t = 0.01
max_lvl = 256
max_volt = 3.3

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

data = []
sleep_t = 0.02

try:
    time_start = time.time()
    value = adc()

    while value < 215:
        print(f"level = {value}, V = {voltage(value)}")
        data.append(voltage(value))
        time.sleep(sleep_t)
        value = adc()

    
    GPIO.output(troyka, 0)
    value = adc()

    while value > 5:
        print(f"level = {value}, V = {voltage(value)}")
        data.append(voltage(value))
        time.sleep(0.2)
        value = adc()
    
    time_stop = time.time()
    exper_time = time_stop - time_start
    print(f"Время - {round(exper_time, 3)} с")
    T_one_exper = exper_time / len(data)
    print(f"Период одного измерения - {round(T_one_exper, 3)}")
    print(f"Частота дискретизации - {round(1 / T_one_exper, 3)}")
    print(f"Шаг квантования АЦП - {round(3.3 / 256, 3)}")

    with open("data.txt", 'w') as file:
        for item in data:
            file.write(f"{item}\n")
    
    with open("settings.txt", 'w') as file:
        file.write(f"{round(1 / T_one_exper, 3)}")
        file.write(f"{round(3.3 / 256, 3)}")

    plt.plot(data)
    plt.show()

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()