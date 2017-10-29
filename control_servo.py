

import RPi.GPIO as GPIO
from time import sleep
import argparse

parser = argparse.ArgumentParser(
    description="performs a variety of operations on a file.",
    epilog="pretty neat, huh?",
    fromfile_prefix_chars='@',
)
parser.add_argument("-A", "--angle", type=int, help="echo the string you use here")
parser.add_argument("-O", "--orientation", help="echo the string you use here")
parser.add_argument('-V', '--version', action="version", version="%(prog)s 0.1")

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)


def set_angle_x(angle):
    GPIO.setup(11, GPIO.OUT)
    duty = angle / 18 + 2
    GPIO.output(11, True)
    pwm = GPIO.PWM(11, 50)
    pwm.start(duty)
    sleep(1)
    GPIO.cleanup()


def set_angle_y(angle):
    GPIO.setup(13, GPIO.OUT)
    duty = angle / 18 + 2
    GPIO.output(13, True)
    pwm = GPIO.PWM(13, 50)
    pwm.start(duty)
    sleep(1)
    GPIO.cleanup()


if __name__ == "__main__":
    args = parser.parse_args()
    setup()
    if args.orientation == "Y":
        set_angle_y(args.angle)
    else:
        set_angle_x(args.angle)
