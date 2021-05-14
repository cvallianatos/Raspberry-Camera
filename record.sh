#!/bin/bash

raspivid -o /home/pi/Projects/Camera/videos/temp.h264  -w 920 -h 540 -t 2700000 -rot 180 -fl 

CURDT=`date +"%Y-%m-%d-%H-%M"`

mv /home/pi/Projects/Camera/videos/temp.h264 /home/pi/Projects/Camera/videos/$CURDT.h264

MP4Box -add /home/pi/Projects/Camera/videos/$CURDT.h264 /home/pi/Projects/Camera/videos/$CURDT.mp4

rclone sync /home/pi/Projects/Camera/videos/$CURDT.mp4 Dropbox:/RPI3/

sudo shutdown -P now