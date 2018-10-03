import ev3dev.ev3 as ev3


def testRobot():
    touchyRobot = BasicBot("Basic")
    touchyRobot.setColorSensor('in1')
    val = 100
    while True:
        val = touchyRobot.readReflect()
        print("Color", val)
    touchyRobot.stop()
    print("Done")


class BasicBot(object):
    """This provides a higher-level interface to Lego robot we've been working
    with."""

    # ---------------------------------------------------------------------------
    # Setup methods, including constructor
    LEFT_MOTOR = 'leftMotor'
    RIGHT_MOTOR = 'rightMotor'
    SERVO_MOTOR = 'servoMotor'

    def __init__(self, robotName):
        """Takes in a string, the name of the robot."""
        self.name = robotName
        self.setMotorPort(self.LEFT_MOTOR, 'outD')
        self.setMotorPort(self.RIGHT_MOTOR, 'outB')
        self.servoMotor = None
        self.leftTouch = None
        self.rightTouch = None
        self.ultraSensor = None
        self.colorSensor = None
        self.gyroSensor = None
        self.leftMotor.stop_action = 'brake'
        self.rightMotor.stop_action = 'brake'
        if self.servoMotor is not None:
            self.servoMotor.stop_action = 'hold'

    def setMotorPort(self, side, port):
        """Takes in which side and which port, and changes the correct variable
        to connect to that port."""
        if side == self.LEFT_MOTOR:
            self.leftMotor = ev3.LargeMotor(port)
        elif side == self.RIGHT_MOTOR:
            self.rightMotor = ev3.LargeMotor(port)
        elif side == self.SERVO_MOTOR:
            self.servoMotor = ev3.MediumMotor(port)
        else:
            print("Incorrect motor description:", side)

    def setTouchSensor(self, side, port):
        """Takes in which side and which port, and changes the correct
        variable to connect to that port"""
        if side == self.LEFT_TOUCH:
            self.leftTouch = ev3.TouchSensor(port)
        elif side == self.RIGHT_TOUCH:
            self.rightTouch = ev3.TouchSensor(port)
        else:
            print("Incorrect touch sensor description:", side)

    def setColorSensor(self, port):
        """Takes in the port for the color sensor and updates object"""
        self.colorSensor = ev3.ColorSensor(port)

    def setUltrasonicSensor(self, port):
        """Takes in the port for the ultrasonic sensor and updates object"""
        self.ultraSensor = ev3.UltrasonicSensor(port)

    def setGyroSensor(self, port):
        """Takes in the port for the gyro sensor and updates object"""
        self.gyroSensor = ev3.GyroSensor(port)

    # ---------------------------------------------------------------------------
    # Methods to read sensor values

    def readTouch(self):
        """Reports the value of both touch sensors, OR just one if only one is connected, OR
        prints an alert and returns nothing if neither is connected."""
        if self.leftTouch is not None and self.rightTouch is not None:
            return self.leftTouch.is_pressed, self.rightTouch.is_pressed
        elif self.leftTouch is not None:
            return self.leftTouch.is_pressed, None
        elif self.rightTouch is not None:
            return None, self.rightTouch
        else:
            print("Warning, no touch sensor connected")
            return None, None

    def readUltra(self):
        """Reports the value of the ultrasonic sensor in centimeters, OR prints an alert
        and returns none if it is not connected."""
        if self.ultraSensor is not None:
            cmData = self.ultraSensor.distance_centimeters
            return cmData
        else:
            print("Warning, no ultrasonic sensor connected")
            return None

    def readReflect(self):
        """Reports the value of the color sensor's reflectance value."""
        if self.colorSensor is not None:
            reflData = self.colorSensor.reflected_light_intensity
            return reflData
        else:
            print("Warning, no color sensor connected")
            return None

    def readAmbientLight(self):
        """Reports the ambient light value from the color sensor."""
        if self.colorSensor is not None:
            ambientData = self.colorSensor.ambient_light_intensity
            return ambientData
        else:
            print("Warning, no color sensor connected")
            return None

    def readColor(self):
        """Reports the color detected by the color sensor, the integers between 0 and 7:
        0: No color, 1: Black, 2: Blue, 3: Green, 4: Yellow, 5: Red, 6: White, 7: Brown."""
        if self.colorSensor is not None:
            colorData = self.colorSensor.color
            return colorData
        else:
            print("Warning, no color sensor connected")
            return None

    def readRGBColor(self):
        """Reports the RGB values detected by the color sensor, in the range from
        0 to 255."""
        if self.colorSensor is not None:
            redVal = int((self.colorSensor.red / 1020) * 255)
            greenVal = int((self.colorSensor.green / 1020) * 255)
            blueVal = int((self.colorSensor.blue / 1020) * 255)
            return (redVal, greenVal, blueVal)
        else:
            print("Warning, no color sensor connected")
            return None

    def readGyroAngle(self):
        """Reports the angle the Gyro sensor has detected that the robot has turned since
        starting up, reported in degrees."""
        if self.gyroSensor is not None:
            angleData = self.gyroSensor.angle
            return angleData
        else:
            print("Warning, no gyro sensor connected")
            return None

    # ---------------------------------------------------------------------------
    # Methods to move robot

    def forward(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional
        time to run (in seconds) and it sets the motors so the robot moves straight forward
        at that speed. This method blocks if a time is specified."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = motorSpeed
        self.rightMotor.speed_sp = motorSpeed
        self._moveRobot(runTime)

    def backward(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional
        time to run (in seconds) and it sets the motors so the robot moves straight forward
        at that speed. This method blocks if a time is specified."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        self.forward(-speed, runTime)

    def turnLeft(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional time
        to run (in seconds) and it sets the motors so the robot turns left in place at
        the given speed. This method blocks if a time is specified until the movement 
        is complete."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = -motorSpeed
        self.rightMotor.speed_sp = motorSpeed
        self._moveRobot(runTime)

    def turnRight(self, speed, runTime=None):
        """Takes in a speed between -1.0 and 1.0 inclusively, and an optional time
        to run (in seconds) and it sets the motors so the robot turns right in place at
        the given speed. This method blocks if a time is specified until the movement 
        is complete."""
        assert -1.0 <= speed <= 1.0
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        motorSpeed = self.leftMotor.max_speed * speed
        self.leftMotor.speed_sp = motorSpeed
        self.rightMotor.speed_sp = -motorSpeed
        self._moveRobot(runTime)

    def stop(self):
        """Turns off the motors and blocks until they have stopped moving."""
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        self.leftMotor.stop()
        self.rightMotor.stop()
        while True:
            lState = self.leftMotor.state
            rState = self.rightMotor.state
            if ('running' not in lState) and ('running' not in rState) and \
                    ('ramping' not in lState) and ('ramping' not in rState):
                break

    def curve(self, leftSpeed, rightSpeed, runTime=None):
        """Takes in two speeds, left motor and right motor speeds, both between
        -1.0 and 1.0 inclusively, and an optional time in seconds for the motors to run.
        It sets the speeds appropriately and runs just like the other movement methods,
        just with different speeds set on each motor. Blocks if a time is specified."""
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        assert -1.0 <= leftSpeed <= 1.0
        assert -1.0 <= rightSpeed <= 1.0
        leftMotorSp = leftSpeed * self.leftMotor.max_speed
        rightMotorSp = rightSpeed * self.rightMotor.max_speed
        self.leftMotor.speed_sp = leftMotorSp
        self.rightMotor.speed_sp = rightMotorSp
        self._moveRobot(runTime)

    def move(self, translateSpeed, rotateSpeed, runTime=None):
        """Takes in two speeds, a translational speed in the direction the robot is facing,
        and a rotational speed both between -1.0 and 1.0 inclusively. Also takes in an 
        optional time in seconds for the motors to run.
        It converts the speeds to left and right wheel speeds, and thencalls curve."""
        wheelDist = 12 * 19.5
        assert self.leftMotor is not None
        assert self.rightMotor is not None
        assert -1.0 <= translateSpeed <= 1.0
        assert -1.0 <= rotateSpeed <= 1.0
        transMotorSp = translateSpeed * self.leftMotor.max_speed
        rotMotorSp = rotateSpeed * 2  # Note that technically rotational speed doesn't have the same units...

        # Here are formulas for converting from translate and rotate speeds to left and right
        # These formulas need to know the distance between the two wheels in order to work
        # which I measured to be 12 cm on my robot. But we have to watch out for units here
        # the speeds are in "ticks" (degrees) per second, so we need to map rotational ticks
        # to centimeters. I measured 360 ticks moving the robot 18.5 cm forward, so 1cm is
        # 19.5 tics. Thus the wheel distance is 12 * 19.5 = 234 ticks.
        leftSpeed = transMotorSp - (rotMotorSp * wheelDist) / 2.0
        rightSpeed = transMotorSp + (rotMotorSp * wheelDist) / 2.0
        print("SPEEDS:", leftSpeed, rightSpeed)
        self.leftMotor.speed_sp = leftSpeed
        self.rightMotor.speed_sp = rightSpeed
        self._moveRobot(runTime)

    def _moveRobot(self, runTime):
        """Helper method, takes in a time in seconds, or time is None if no time limit, 
        and it runs the motors at the current speed either forever or for the given time.
        Blocks and waits if a time is given."""
        if runTime is None:
            self.leftMotor.run_forever()
            self.rightMotor.run_forever()
        else:
            milliSecTime = runTime * 1000.0
            self.leftMotor.run_timed(time_sp=milliSecTime)
            self.rightMotor.run_timed(time_sp=milliSecTime)
            self.rightMotor.wait_until_not_moving()


# Sample of how to use this
if __name__ == "__main__":
    testRobot()