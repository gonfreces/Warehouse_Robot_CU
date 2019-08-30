"""
Game: StopIt!
* Its a simple game consisting of five LED lights and one pushbutton switch. 
* The LEDs flash in a sequence and the player must press the button when the Green LED light is lit. 
* The speed at which the lights flash increases until the player presses the button at the wrong time.

Player: Raspbery Pi Camera
* Using a RPi camera to detect and send a signal that swicthes the button on

"""

from __future__ import print_function
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np
from difflib import SequenceMatcher
import sys
import time 
import RPi.GPIO as GPIO
import time

#def gd2();
b = 4
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(b,GPIO.OUT)


camera = PiCamera()
camera.resolution = (400, 300)
camera.framerate = 15
camera.start_preview()
time.sleep(2)
rawCapture = PiRGBArray(camera, size=(400, 300))
    
# allow the camera to warmup
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # grab the raw NumPy array representing the image, then initialize the timestamp
            # and occupied/unoccupied text
    try:      
            cap = frame.array
     
            # show the frame
            cv2.imshow("Frame", cap)
            key = cv2.waitKey(5) & 0xFF
            #cv2.line(cap, (0,0),(400,300),(255,0,0),15)
            #cv2.imshow("f2", cap)
            # clear the stream in preparation for the next frame
            
            #detect green
            hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV) #image array convert to hsv
            
            #create a mask for only green colored sections to show
            mask = cv2.inRange(hsv, (50,150,200),(70,255,255))
            
            #slice the green part
            imask = mask>0
            green = np.zeros_like(cap, np.uint8) #make others black
            green[imask] = cap[imask] # pass coordinates but doubt
            cv2.imshow("f2", green)
            if mask.any()>0:
                print("Found")
                GPIO.output(b, GPIO.HIGH)
            rawCapture.truncate(0)
            
            # if the `q` key was pressed, break from the loop
            if key == 27:
                    break
    except KeyboardInterrupt:
            raise
        

cv2.destroyAllWindows()
 
