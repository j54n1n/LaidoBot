#!/usr/bin/env python3

import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        self.driveFrontLeft  = wpilib.Victor(0)
        self.driveFrontRight = wpilib.Victor(1)
        self.driveRearLeft   = wpilib.Victor(2)
        self.driveRearRight  = wpilib.Victor(3)
        self.launcherBelt = wpilib.Victor(4)
        self.launcherBarrel = wpilib.Victor(5)
        self.tankDrive = wpilib.RobotDrive(
            self.driveFrontLeft, self.driveRearLeft,
            self.driveFrontRight, self.driveRearRight
        )
        self.stick = wpilib.Joystick(0);
        #self.timer = wpilib.Timer();
        #self.timer.start();
        self.launcherBarrel.set(0);
        self.launcherBelt.set(0);
        """
        You should be able to connect to the camera using SmartDashboard,
        the default LabVIEW Dashboard, or if you point your browser at
        http://roborio-XXXX-frc.local:1181.
        """
        wpilib.CameraServer.launch("vision.py:main")

    def teleopInit(self):
        axisCount = self.stick.getAxisCount()
        buttonCount = self.stick.getButtonCount()

        #print("AxisCount = " + str(axisCount))
        for axis in range(0, axisCount):
            try:
                axisChannel = self.stick.getAxisChannel(axis)
                #print(str(axis) + ": axisChannel = " + str(axisChannel))
            except IndexError:
                pass
        #print("ButtonCount = " + str(buttonCount))
        for button in range(1, buttonCount + 1):
            try:
                rawButton = self.stick.getRawButton(button)
                #print(str(button) + ": rawButton = " + str(rawButton))
            except IndexError:
                pass

    def teleopPeriodic(self):
        self.tankDrive.arcadeDrive(self.stick)
        launcherVelocity = self.stick.getZ()
        self.launcherBelt.set(launcherVelocity)
        if launcherVelocity < 0:
            self.launcherBarrel.set(launcherVelocity)
        else:
            self.launcherBarrel.set(0)
        #if self.timer.hasPeriodPassed(0.2):
        #    pass

    def autonomousInit(self):
        self.driveFrontLeft.set(0)
        self.driveFrontRight.set(0)
        self.driveRearLeft.set(0)
        self.driveRearRight.set(0)

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
