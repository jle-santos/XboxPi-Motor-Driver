# Controls Adafruit Motor Driver with Xbox Controls

'''
Motor Configuration
{1} -FRONT- {2}
    
{3} - BACK- {4}

'''

from adafruit_motorkit import MotorKit
import xbox

# Create Motor Object
kit = MotorKit()

# Create joystick object
joy = xbox.Joystick()

kit.motor1.throttle = 0
kit.motor2.throttle = 0
kit.motor3.throttle = 0
kit.motor4.throttle = 0

print("Starting Motor Control")
print("Press BACK button to exit")

while not joy.Back():
    # Normalize joystick values
    driveX = joy.leftX()
    driveY = joy.leftY()
    print("Left X/Y: ", '{0:.2}'.format(driveX), "/", '{0:.2}'.format(driveY), "DIR: ", end='')
    # Check if the left stick is turning, else its forward/back
    if driveX > 0.7:
        print(" RIGHT"),
        #kit.motor1.throttle = driveX
        #kit.motor3.throttle = driveX
        #kit.motor2.throttle = driveX # Spin opposite way
        kit.motor4.throttle = driveX # Spin opposite way
    elif driveX < -0.7:
        print(" LEFT"),
        #kit.motor1.throttle = driveX
        #kit.motor3.throttle = driveX
        #kit.motor2.throttle = driveX # Spin opposite way
        kit.motor4.throttle = driveX # Spin opposite way
    elif driveY < -0.2:
        print(" BACKWARD"),
        #kit.motor1.throttle = driveY
        #kit.motor3.throttle = driveY
        #kit.motor2.throttle = driveY 
        kit.motor4.throttle = driveY
        
    elif driveY > 0.2:
        print(" FORWARD"),
        #kit.motor1.throttle = driveY
        #kit.motor3.throttle = driveY
        #kit.motor2.throttle = driveY 
        kit.motor4.throttle = driveY 
    
    else:
        print(" STOP"),
        kit.motor1.throttle = 0
        kit.motor3.throttle = 0
        kit.motor2.throttle = 0 # Spin opposite way
        kit.motor4.throttle = 0 # Spin opposite way

