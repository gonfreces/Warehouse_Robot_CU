# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import smbus
import time

#string parser
from Str_parser import star

#publisher
from mq_pub import mq_pub
ch = "1"
ip = "10.201.87.203"
text = ""
m1 = mq_pub(ch,ip,text)

#subscribe to master pi
import paho.mqtt.client as mqtt
MQTT_SERVER = "localhost"
MQTT_PATH_1 = "1"

from picamera import PiCamera
bus = smbus.SMBus(1)
address = 0x04

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
i = 0 # action iteration variable
p = 0 # counter declared to avoid pub two times
k = 0 #counter for direction variable to send once
while True:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF

    if p == 0:
        #Scan assignment QR code
        for barcode in barcodes:
            barcodeData = barcode.data.decode("utf-8")
            fi = open("start.txt", "w")
            fi.write(barcodeData)
            fi.close()
            #scp - do this !!! - Parse the string here
            global x1 = [2,2,2,2,2,2,3,2,2,2,2,2] #All x coordiantes of qrcode
            global y1  = [2,2,2,2,2,2,3,2,2,2,2,2]#All y co-ordinates of qrcode
            global dir = ['fwd','fwd','left','right','fwd','fwd','left','fwd','fwd','fwd','fwd']#all actions
            global backt = 1 #1 if a backkward turn in motion
            global rackt = 'right' #rack turn
            global rqx = 3#rack qr code x
            global rqy = 3#rack qr code y
            global pno = 'pallet 57' #pallet no
            global prow = row 3 #palletrow - height
            break
        #send all info Pallet Pi
        text = pno
        m1.pub_me()
        text = rackt
        m1.pub_me()
        text = "stop"
        m1.pub_me()

        #get picam to desired height - activate stepper
        bus.write_byte(address, int(ord(6))) #stepper
        time.sleep(2.0)
        bus.write_byte(address, int(ord(8)))#deactivate stepper
        p = p+1


    if k == 0:
    # get dir array and command arduino/redboard
        if dir[i] == "fwd":
            bus.write_byte(address, int(ord(1))) #lane follower
            k = 1
        elif dir[i] == "right":
            bus.write_byte(address, int(ord(4))) #right
            k = 1
        elif dir[i] == "left":
            bus.write_byte(address, int(ord(5))) #left
            k = 1

    #DOCKING

    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        #bus.write_byte(address, int(ord(j1)))
        (x, y, w, h) = barcode.rect
        #print(h,w)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        #parsing qr code on ground
        #-----------------------------
        #spa = star(barcodeData)
        #spa1 = spa.star1()
        #-----------------------------
        spa1 = [2,2,3,3]
        if  spa1[0] == x1[i+1] and spa1[1] == y1[i+1]:
            i = i+1 #onto next node
            k = 0 

        pal1 = " "
        pal2 = " "
        if spa1[2] == rqx and spa1[3] == rqy:
            bus.write_byte(address, int(ord(0))) #stop

            client = mqtt.Client()
            def on_connect(client,userdata, flags, rc):
                print("connected with result code"+str(rc))
            	#client.subscribe(self.path)
                client.subscribe(MQTT_PATH_1)

            def on_message(client, userdata, msg):
            	print(msg.topic+" "+str(msg.payload))
            	p1 = str(msg.payload)
                #store pallet no(string) in var
                if p1 == "pallet_here":
                    global pal1 = p1
                elif p1 == "pallet_turn":
                    global pal2 = p1
                elif p1 == "stop":
                    client.disconnect()

            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(MQTT_SERVER, 1883,60)
            client.loop_forever()

            if pal1 == "pallet_here":
                bus.write_byte(address, int(ord(0))) #stop
                time.sleep(2)
            if pal2 == "pallet_turn":
                if pal2 == 'right':
                    bus.write_byte(address, int(ord(4))) #turn  right towards rack
                    time.sleep(3)
                    bus.write_byte(address, int(ord(0))) #stop
                    time.sleep(2)
                else pal2 == 'left':
                    bus.write_byte(address, int(ord(5))) #turn left towards rack
                    time.sleep(3)
                    bus.write_byte(address, int(ord(0))) #stop
                    time.sleep(2)
            #start alignment code
            text = "start_align"
            m1.pub_me()
            #text = "stop"
            #m1.pub_me()

            #get jerk directions from Pallet Pi and send to arduino
            client = mqtt.Client()
            client.connect(MQTT_SERVER, 1883,60)
            client.loop_start()
            def on_connect(client,userdata, flags, rc):
                print("connected with result code"+str(rc))
            	#client.subscribe(self.path)
                client.subscribe(MQTT_PATH_1)

            def on_message(client, userdata, msg):
            	print(msg.topic+" "+str(msg.payload))
            	global p1 = str(msg.payload)
                #store pallet no(string) in var
                if p1 == "align_done":
                    global pal1 = p1
                elif p1 == "right":
                    global pal1 = p1
                elif p1 == "left":
                    global pal1 = p1
                elif p1 == "stop":
                    client.disconnect() #break onl when this
                    client.loop_stop() # while loop below will still run until this gets hit amd stop breaks them both

            client.on_connect = on_connect
            client.on_message = on_message

            #client.loop_forever()
            while (pal1 == "left") or (pal1 == "right") or (pal1 != "align_done")
                if pal1 == "left":
                    bus.write_byte(address, int(ord(5))) #left
                if pal1 == "right":
                    bus.write_byte(address, int(ord(4))) #right
            if pal1 =="align_done":
                bus.write_byte(address, int(ord(0)))#stop

            #alignment done
            #Pallet pickup code
            #go forward
            bus.write_byte(address, int(ord(2)))#forward
            time.sleep(3.0)
            #stop
            bus.write_byte(address, int(ord(0)))#stop
            time.sleep(2.0)
            #stepper up
            bus.write_byte(address, int(ord(6)))#stepper up
            time.sleep(3.0)
            #stepper stop
            bus.write_byte(address, int(ord(8)))# stepper stop
            time.sleep(1.0)
            #come back to org position - back
            bus.write_byte(address, int(ord(3)))# backward
            time.sleep(2.0)
            #stop
            bus.write_byte(address, int(ord(0)))#stop
            time.sleep(2.0)
            #turn to face as org position
            if backt == 0: # no 180 deg change
                if rackt == "right":#opposite turn
                    bus.write_byte(address, int(ord(5)))#left
                    time.sleep(3.0)
                    #stop
                    bus.write_byte(address, int(ord(0)))#stop
                    time.sleep(2.0)
                elif rackt == "left": #opposite turn
                    bus.write_byte(address, int(ord(4)))#right
                    time.sleep(2.0)
                    #stop
                    bus.write_byte(address, int(ord(0)))#stop
                    time.sleep(2.0)
            elif backt == 1: # 180 deg change
                if rackt == "right":#same turn
                    bus.write_byte(address, int(ord(4)))#right
                    time.sleep(3.0)
                    #stop
                    bus.write_byte(address, int(ord(0)))#stop
                    time.sleep(2.0)
                elif rackt == "left": #same turn
                    bus.write_byte(address, int(ord(5)))#left
                    time.sleep(3.0)
                    #stop
                    bus.write_byte(address, int(ord(0)))#stop
                    time.sleep(2.0)
            #wait for the turn
            time.sleep(1.0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
