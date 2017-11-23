#!/usr/bin/env python3

from cscore import CameraServer

def main():
    CAM_PX_WIDTH = 320
    CAM_PX_HEIGHT = 240
    CAM_FPS = 30
    
    cameraServer = CameraServer.getInstance()
    cameraServer.enableLogging()

    """
    Sometimes the first and second camera swap!?
    When using multiple USB cameras, Linux will sometimes order the cameras
    unpredictably – so camera 1 will become camera 0. Sometimes.
    The way to deal with this is to tell cscore to use a specific camera by
    its path on the file system. First, identify the cameras dev paths by
    using SSH to access the robot and execute find /dev/v4l. You should see
    output similar to this:
    /dev/v4l
    /dev/v4l/by-path
    /dev/v4l/by-path/pci-0000:00:1a.0-usb-0:1.4:1.0-video-index0
    /dev/v4l/by-path/pci-0000:00:1d.0-usb-0:1.4:1.2-video-index0
    /dev/v4l/by-id
    ...
    What you need to do is figure out what paths belong to which camera, and
    then when you start the camera server, pass it a name and a path via:
    usb1 = cs.startAutomaticCapture(
            name="cam1",
            path='/dev/v4l/by-id/some-path-here'
    )
    usb2 = cs.startAutomaticCapture(
            name="cam2",
            path='/dev/v4l/by-id/some-other-path-here'
    )
    Note:
    The Microsoft Lifecam cameras commonly used in FRC don’t have unique IDs
    associated with them, so you’ll want to use the by-path versions of the
    links if you are using two Lifecams.
    """
    cam0 = cameraServer.startAutomaticCapture(dev=0)
    cam1 = cameraServer.startAutomaticCapture(dev=1)

    cameraServer.waitForever()
