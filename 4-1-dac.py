import RPi.GPIO as GPIO

def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]
    
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        num = input()

        if num == 'q':
            break
        elif not is_number(num):
            print("Введено не число")
            continue
        elif int(num) != float(num):
            print("Введено не целое число")
            continue

        num = int(num)

        if num < 0:
            print("Введено отрицательное значение")
            continue
        elif num > 255:
            print("Число вне диапозона")
            continue 

        print(f"Напряжение: {round((num / 255) * 3.3, 2)}")
        print(decimal2binary(num))
        GPIO.output(dac, decimal2binary(num))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
