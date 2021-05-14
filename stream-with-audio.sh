#!/bin/bash

cd /home/pi/picam

/home/pi/picam/picam --alsadev hw:1,0 --rotation 180 &

sleep 10

touch /home/pi/picam/hooks/start_record

sleep 10

touch /home/pi/picam/hooks/stop_record

killall picam

CURDT=$(date +"%Y-%m-%d-%H-%M")

TRGFILE=$(ls -t /home/pi/picam/rec/archive  | head -n1)

ffmpeg -i /home/pi/picam/rec/archive/$TRGFILE -c:v copy -c:a copy -bsf:a aac_adtstoasc /home/pi/picam/rec/archive/$CURDT.mp4
 
rclone sync /home/pi/picam/rec/archive/$CURDT.mp4  Dropbox:/RPI3/ 

rm /home/pi/picam/rec/archive/$TRGFILE 

#sudo shutdown -P now
