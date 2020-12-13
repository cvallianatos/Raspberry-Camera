#!/bin/bash

raspivid -o - -w 920 -h 540 -t 0 -rot 180 -fl -a 12 -ae 10,15,10 | tee /home/pi/Projects/Camera/videos/temp.h264 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264

CURDT=`date +"%Y-%m-%d-%H-%M"`

mv /home/pi/Projects/Camera/videos/temp.h264 /home/pi/Projects/Camera/videos/$CURDT.h264

MP4Box -add /home/pi/Projects/Camera/videos/$CURDT.h264 /home/pi/Projects/Camera/videos/$CURDT.mp4

rclone sync /home/pi/Projects/Camera/videos/$CURDT.mp4 Dropbox:/RPI3/