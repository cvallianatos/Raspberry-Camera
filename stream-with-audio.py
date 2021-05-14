import io
import time
import os
from datetime import datetime

os.system("cd /home/pi/picam")

os.system("/home/pi/picam/picam --alsadev hw:1,0 --rotation 180 &")

os.system("touch /home/pi/picam/hooks/start_record")

time.sleep(3600)

os.system("touch /home/pi/picam/hooks/stop_record")

os.system("killall picam")

now = datetime.now()
dt_string = now.strftime("%Y-%m-%d-%H-%M")
#CURDT=`date +"%Y-%m-%d-%H-%M"`

#TRGFILE='ls -t /home/pi/picam/rec  | head -n1'

#ffmpeg -i /home/pi/picam/rec/$TRGFILE  -c:v copy -c:a copy -bsf:a aac_adtstoasc /home/pi/picam/rec/$CURDT.mp4
 
#rclone sync /home/pi/picam/rec/$CURDT.mp4  Dropbox:/RPI2/ 

#rm /home/pi/picam/rec/$TRGFILE 

#sudo shutdown -P now
