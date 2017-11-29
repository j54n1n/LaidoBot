'''

Controller commands

'''

import wpilib


class Joy:
    def __init__(self, motors):
        self.motors = motors
        self.my_stick = wpilib.Joystick(0)
        # self.barrel_speed = 0
        # self.belt_speed = 0
        # self.gear_speed = 0


    def switch(self, status):
        self.button5 = self.my_stick.getRawButton(5)
        self.button6 = self.my_stick.getRawButton(6)
        self.button7 = self.my_stick.getRawButton(7)
        self.button8 = self.my_stick.getRawButton(8)

        if self.button5:
            status = 5
        elif self.button6:
            status = 6
        elif self.button7:
            status = 7
        elif self.button8:
            status = 8

        if status == 5:
            if self.getAccelerator() < 0:
                print("porcodio 1")
                self.motorRamp(self.getAccelerator(), self.motors.launcherBarrel)
                self.motorRamp(self.getAccelerator(), self.motors.launcherBelt)
                self.motors.gear.set(0)
            else:
                print("porcodio 2")
                self.all_util_to_zero()
        elif status == 6:
            if self.getAccelerator() > 0:
                print("porcodio 3")
                self.motors.launcherBarrel.set(0)
                self.motorRamp(-self.getAccelerator(), self.motors.launcherBelt)
                self.motors.gear.set(0)
            else:
                self.all_util_to_zero()
        elif status == 7:
            print("porcodio 4")
            self.motors.launcherBarrel.set(0)
            self.motors.launcherBelt.set(0)
            self.motorRamp(self.getAccelerator(), self.motors.gear)
        elif status == 8:
            self.all_util_to_zero()

        return status

    def getAccelerator(self):
        return self.my_stick.getZ()

    def motorRamp(self, stickSetPoint, motorDriver):
        deltaSpeed = 0.01
        motorSetPoint = motorDriver.get()
        if stickSetPoint > motorSetPoint:
            motorDriver.set(motorSetPoint + deltaSpeed)
        elif stickSetPoint < motorSetPoint:
            motorDriver.set(motorSetPoint - deltaSpeed)

    def rawMotorRamp(self, stickSetPoint, motorDriver):
        deltaSpeed = 0.01
        motorSetPoint = motorDriver.get()
        if stickSetPoint > motorSetPoint:
            newSetPoint = motorSetPoint + deltaSpeed
        elif stickSetPoint < motorSetPoint:
            newSetPoint = motorSetPoint - deltaSpeed
        if motorSetPoint < 1.0 and motorSetPoint > 0.0:
            motorDriver.set(newSetPoint)


    # def set_utility_motors_speed(self, motor):
    #     print("porcodio 6")
    #     self.motorRamp(self.getAccelerator(), motor)

    def all_util_to_zero(self):
        self.motors.launcherBarrel.set(0)
        self.motors.launcherBelt.set(0)
        self.motors.gear.set(0)
