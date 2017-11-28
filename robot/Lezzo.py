'''

Controller commands

'''

import wpilib
from wpilib import Joystick
from LaidoMap import Motors

class Joy:
    def __init__(self):
        Joy = wpilib.Joystick
        self.my_stick = wpilib.Joystick(0)
        self.button5 = Joy.getRawButton(self.my_stick, 5)
        self.button6 = Joy.getRawButton(self.my_stick, 6)
        self.button7 = Joy.getRawButton(self.my_stick, 7)
        #self.quit_button = Joystick.getRawButton(?)  FIXME
        self.launcher_velocity = self.my_stick.getZ()

    def switch(self, status):
        if self.button5:
            status = 5
        elif self.button6:
            status = 6
        elif self.button7:
            status = 7
        # elif self.quit_button:
        #     #start other activity
        #     pass

        speed_index = self.launcher_velocity
        if status == 5:
            if speed_index < 0:
                self.set_speed(speed_index, Motors.launcherBelt)
            else:
                self.set_speed(0, Motors.launcherBelt)
        elif status == 6:
            self.set_speed(-speed_index, Motors.launcherBelt)
        elif status == 7:
            self.set_speed(speed_index, Motors.lift)

    def set_speed(self, speed, motor):
        speed_irl = speed
        if speed_irl == 0:
            motor.set(0)
        elif speed_irl == speed:
            pass
        elif speed_irl < speed:
            motor.set(speed_irl + 0.01)
        elif speed_irl > speed:
            motor.set(speed_irl - 0.01)

    def is_pressed(self):
        if self.button5 or self.button6 or self.button7:
            return True
