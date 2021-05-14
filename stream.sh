#!/bin/bash

raspivid -o - -w 920 -h 540 -t 0 -rot 180 -fl -a 12 -ae 10,15,10 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
