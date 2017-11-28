'''

Motors mapping

'''

import wpilib

class Motors:
    driveFrontLeft = wpilib.Victor(0)
    driveFrontRight = wpilib.Victor(1)
    driveRearLeft = wpilib.Victor(2)
    driveRearRight = wpilib.Victor(3)
    launcherBelt = wpilib.Victor(4)
    launcherBarrel = wpilib.Victor(5)
    lift = wpilib.Victor(6) #FIXME

