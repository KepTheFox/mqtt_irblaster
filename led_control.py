import OPi.GPIO as GPIO
import time

LED_PIN = 35

GPIO.setboard(GPIO.PC2)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def led_on():
    print("LED ON")
    GPIO.output(LED_PIN, 1)

def led_off():
    print("LED OFF")
    GPIO.output(LED_PIN, 0)