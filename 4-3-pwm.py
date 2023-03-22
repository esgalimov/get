import RPi.GPIO as GPIO


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

pwm = GPIO.PWM(15, 100)
pwm.start(0)

try:
    while True:
        koeff = input()

        if koeff == 'q':
            break
        
        if not is_number(koeff):
            print("Введено не число")
            continue
        koeff = float(koeff)
        if koeff < 0 or koeff > 100:
            print("Неверное число")
            continue

        print(f"Напряжение - {round((koeff / 100) * 3.3, 2)}")
        pwm.stop()
        pwm.start(koeff)

finally:
    pwm.stop()
    GPIO.cleanup()

