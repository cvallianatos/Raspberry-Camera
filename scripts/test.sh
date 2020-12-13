#!/bin/bash

CURDT=`date +"%Y-%m-%d-%H-%M"`

echo Current Date and Time is: $CURDT

ls -al > $CURDT.txt
