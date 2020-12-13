import os
import time
import datetime
from time import sleep
from picamera import PiCamera

def settings():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    
    myFlag = True
    while myFlag: 
        print("Settings")
        print("---------")
        print("(I) Initialize Database")
        print("(D) Set configuration parameters")
        print("(E) Return to Main Menu") 
        myOption = input()
        myOption = myOption.upper()

        if myOption == "E":
            myFlag = False
        elif myOption == "I":
            initializeDb()
        elif myOption == "D":
            print("D")
        else:
            print("Please select a valid option.")
            print("Press enter to continue.")
            input()
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    return

def startVideoStream():
    return

def startVideoRecording():
    return
    
def takeSnapshots():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.rotation = 270    
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('/home/pi/Projects/Camera/images/snap.jpg')

    os.system('mutt -a snap.jpg -s "Snapshot from PI 3" -- tbrahe20@gmail.com < /home/pi/Projects/Camera/scripts/mail.txt ')
    return