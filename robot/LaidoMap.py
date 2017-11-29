'''

Motors mapping

'''

import wpilib

class Motors:
    def __init__(self):
        self.driveFrontLeft = wpilib.Victor(0)
        self.driveFrontRight = wpilib.Victor(1)
        self.driveRearLeft = wpilib.Victor(2)
        self.driveRearRight = wpilib.Victor(3)
        self.launcherBelt = wpilib.Victor(4)
        self.launcherBarrel = wpilib.Victor(5)
        self.gear = wpilib.Victor(6) #FIXME


