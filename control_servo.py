import RPi.GPIO as GPIO
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)


def set_angle_x(angle):
    duty = angle / 18 + 2
    GPIO.output(13, True)
    pwm = GPIO.PWM(13, 50)
    pwm.ChangeDutyCycle(duty)
    sleep(1)


def set_angle_y(angle):
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm = GPIO.PWM(11, 50)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
