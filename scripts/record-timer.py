import io
import time
import picamera
import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M")

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.rotation = 270    
    my_video = "/home/pi/Projects/Camera/video/" + dt_string + ".h264"
    camera.start_recording(my_video)
    
    time.sleep(3600)
   
    camera.wait_recording(5)
    camera.stop_recording()

    os.system("rclone sync " + my_video + " Dropbox:/RPI4/")

    os.system("sudo shutdown -P now")
