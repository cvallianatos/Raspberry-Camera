import os
import common as cmn
import glob

def main():
    # Main program

    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

    myFlag = True
    while myFlag: 
        print("Main Menu")
        print("---------")
        print("(W) Start camera stream to Web")
        print("(V) Start video recording to file")
        print("(P) Start picture snapshots")
        print("(S) Settings")
        print("(E) Exit") 

        myOption = input()
        myOption = myOption.upper()

        if myOption == "E":
            myFlag = False
        elif myOption == "W":
            cmn.startVideoStream()
        elif myOption == "V":
            cmn.startVideoRecording()
        elif myOption == "P":
            cmn.takeSnapshots()
        elif myOption == "S":
            cmn.settings()
        else:
            print("Please select a valid option.")
            print("Press enter to continue.")
            myOption = input()
    return

if __name__ == '__main__':
    main()