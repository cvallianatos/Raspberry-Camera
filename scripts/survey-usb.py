import os
from picamera import PiCamera
from time import sleep

def main():
    # Main program

    os.system('fswebcam --rotate 270 /home/pi/Projects/Camera/images/snap.jpg')
    os.system('mutt -a /home/pi/Projects/Camera/images/snap.jpg -s "Snapshot from PI 1" -- tbrahe20@gmail.com < /home/pi/Projects/Camera/scripts/mail.txt')
    return

if __name__ == '__main__':
    main()
