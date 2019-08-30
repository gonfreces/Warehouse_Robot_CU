# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import RPi.GPIO as GPIO
import time
import argparse
import datetime
import imutils
import cv2

#string parser
from Str_parser import star

#servo
from servo_pi_1 import servo
global turn = "right"#default
se = servo(turn)

#publisher
from mq_pub import mq_pub
ch = "2"
ip = "10.201.73.61"
text = ""
m1 = mq_pub(ch,ip,text)

from picamera import PiCamera
# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(usePiCamera=True).start()
time.sleep(5.0)

#subscribe to master pi
import paho.mqtt.client as mqtt
MQTT_SERVER = "localhost"
MQTT_PATH_1 = "1"

client = mqtt.Client()
def on_connect(client,userdata, flags, rc):
    print("connected with result code"+str(rc))
	#client.subscribe(self.path)
    client.subscribe(MQTT_PATH_1)

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	global p1 = str(msg.payload)
    #store pallet no(string) in var
    if p1[0] == "p":
        global pno = p1
    #Get flag to turn servo pi
    elif p1 == "right":
        se.serv()
    elif p1 == "left":
        global turn = "left"
        se.serv()
    elif p1 == "stop"
        client.disconnect()

client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883,60)
client.loop_forever()

# counter declared to avoid reinitialisation of Pallet here
p = 0 # may be needed to define global

#OpenCV barcode and QR code scanner with ZBarPython
# loop over the frames from the video stream
while True:
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)
    key = cv2.waitKey(1) & 0xFF

    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        print(x,y,w,h)
        # show the output frame
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF

        #only check if QR pallet - Once! - so 'p' var is used
        if len(barcodeData) == 12:
            spa = star(barcodeData[0:len(barcodeData)-1])
            spa1 = spa.star1()
        else:
            spa = star(barcodeData)
            spa1 = spa.star1()
        if p == 0: #runs only once when target pallet detected
            if spa1 == pno: #spa1 =pallet 06
                global text = "pallet_here" #stop motors
                m1.pub_me() #send flag that pallet is here to master pi
                global turn = "home"
                se.serv()
                text = "pallet_turn" #turn towards rack
                m1.pub_me()
                text = "stop" #turn towards rack
                m1.pub_me()
            p = p + 1 # = 1

        if p == 1:
            #waiting for start align code after robot is in front of pallet
            client = mqtt.Client()
            def on_connect(client,userdata, flags, rc):
                print("connected with result code"+str(rc))
                client.subscribe(MQTT_PATH_1)

            def on_message(client, userdata, msg):
                print(msg.topic+" "+str(msg.payload))
                global p1 = str(msg.payload)
                if p1 == "start_align": #stall untill you get start align
                    #global pal = p1
                    global p = p+1 # = 2
                    print(p)
                    client.disconnect()
                #elif p1 == "stop":
                    #global p = p+1 # = 2
                    #client.disconnect()

            client.on_connect = on_connect
            client.on_message = on_message
            client.connect(MQTT_SERVER, 1883,60)
            client.loop_forever()

        #if pal1 == start_align
        # qr code alignment starts
        if p == 2:
            ed = x + (w / 2)    # estimated distance
            #print(x,w,ed)
            if ed < 200:
                if turn == "left":#qr code behind robot center is ahead
                    #bus.write_byte(address, int(ord(j[8])))   #turn left
                    text = "left"
                    m1.pub_me()#backwards jerks - motor 2
                    text = "stop"#stop the channel to let the other side continue its task
                    m1.pub_me() #tweak the time delay value
                    #time.sleep(0.2)#send multiple commands fast to create jerks

                elif turn == "right":#qr code behind robot center is ahead
                    #bus.write_byte(address, int(ord(j[8])))   #turn right
                    text = "right"
                    m1.pub_me()#backwards jerks - motor 1
                    text = "stop"#stop the channel to let the other side continue its task
                    m1.pub_me() #tweak the time delay value
                    #time.sleep(0.2)#send multiple commands fast to create jerks
            #once in center - not using for now
            #if abs(w-h)<=20 :
            elif ed > 200:
                p = p + 1 # = 3
                text = "align_done"
                m1.pub_me()
                text = "stop"#stop the channel to let the other side continue its task
                m1.pub_me()
                break
    # if the `q` key was pressed, break from the loop
    if p == 3:
        print("I am done")
        break

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
