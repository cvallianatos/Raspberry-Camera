import os
from picamera import PiCamera
from time import sleep

def main():
    # Main program

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.rotation = 270    
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('/home/pi/Projects/Camera/images/snap.jpg')

    os.system('mutt -a /home/pi/Projects/Camera/images/snap.jpg -s "Snapshot from PI 3" -- tbrahe20@gmail.com < /home/pi/Projects/Camera/scripts/mail.txt ')
    return

if __name__ == '__main__':
    main()