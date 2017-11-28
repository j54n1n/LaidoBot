#!/usr/bin/env python3

import wpilib
from LaidoMap import Motors
from Lezzo import Joy
class MyRobot(wpilib.IterativeRobot):
    def robotInit(self):
        self.tankDrive = wpilib.RobotDrive(Motors.driveFrontLeft, Motors.driveRearLeft,
                                           Motors.driveFrontRight, Motors.driveRearRight)
        self.joy = Joy()
        self.stick = self.joy.my_stick
        # self.timer = wpilib.Timer()
        # self.timer.start()
        Motors.launcherBarrel.set(0)
        Motors.launcherBelt.set(0)

    def teleopInit(self):
        axis_count = self.stick.getAxisCount()
        button_count = self.stick.getButtonCount()
        self.status = 5

        # print("AxisCount = " + str(axis_count))
        for axis in range(0, axis_count):
            try:
                axis_channel = self.stick.getAxisChannel(axis)
                # print(str(axis) + ": axis_channel = " + str(axis_channel))
            except IndexError:
                pass
        # print("ButtonCount = " + str(button_count))
        for button in range(1, button_count + 1):
            try:
                raw_button = self.stick.getRawButton(button)
                # print(str(button) + ": raw_button = " + str(raw_button))
            except IndexError:
                pass

    def teleopPeriodic(self):
        self.tankDrive.arcadeDrive(self.stick)
        self.joy.switch(self.status)



    def autonomousInit(self):
        Motors.driveFrontLeft.set(0)
        Motors.driveFrontRight.set(0)
        Motors.driveRearLeft.set(0)
        Motors.driveRearRight.set(0)

    def autonomousPeriodic(self):
        pass

    def robotPeriodic(self):
        pass

    def disabledPeriodic(self):
        pass

    def disabledInit(self):
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)