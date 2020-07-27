# Controls Adafruit Motor Driver with Xbox Controls

from adafruit_motorkit import MotorKit
import time
import xbox

kit = MotorKit()

print("Hello world")

print("turning all motors")

kit.motor1.throttle = -1
kit.motor2.throttle = -1
kit.motor3.throttle = -1
kit.motor4.throttle = -1

time.sleep(2)

kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0

