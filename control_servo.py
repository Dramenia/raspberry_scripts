####
#
#
####
import RPi.GPIO as GPIO
from time import sleep
import argparse

parser = argparse.ArgumentParser(
    description="Script to move the pan/tilt of the pi camera",
    epilog="orientation Y = tilt, X = pan",
    fromfile_prefix_chars='@',
)
parser.add_argument("-A", "--angle", dest="angle", type=int, help="echo the string you use here")
parser.add_argument("-O", "--orientation", dest="orientation", type=str, help="echo the string you use here")
parser.add_argument('-V', '--version', action="version", version="%(prog)s 0.1")

angle_limits = {"Y": [20, 180, 13], "X": [0, 180, 11]}


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)


def set_angle(angle, port):
    GPIO.setup(port, GPIO.OUT)
    GPIO.output(port, True)
    pwm = GPIO.PWM(port, 50)
    pwm.start(duty_cycle(angle))
    sleep(1)
    GPIO.cleanup()


def duty_cycle(angle):
    return float(angle) / 18.0 + 2


def angle_check(angle, min_angle, max_angle):
    if min_angle < angle < max_angle:
        return angle
    elif min_angle >= angle:
        return min_angle
    else:
        return max_angle

if __name__ == "__main__":
    args = parser.parse_args()
    setup()
    if args.orientation.upper() == "Y":
        set_angle(angle_check(args.angle, angle_limits["Y"][0], angle_limits["Y"][1]), angle_limits["Y"][2])
    else:
        set_angle(angle_check(args.angle, angle_limits["X"][0], angle_limits["X"][1]), angle_limits["X"][2])
