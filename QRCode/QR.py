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

bus = smbus.SMBus(1);
address = 0x04

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# open the output CSV file for writing and initialize the set of
# barcodes found thus far
csv = open(args["output"], "w")
found = set()
p=0
#OpenCV barcode and QR code scanner with ZBarPython
# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# find the barcodes in the frame and decode each of the barcodes
	barcodes = pyzbar.decode(frame)
	cv2.imshow("windw",frame)
	key =cv2.waitKey(1) & 0xFF
	#time.sleep()

	j = ['1','2','3','4']
	if not barcodes:
		print("not here",p)
		p=p+1
		if p>=3:
			bus.write_byte(address, int(ord(j[0])))
		time.sleep(3.0)
		#if  barcodes:
		#	break;
	else:
		p=0
                bus.write_byte(address, int(ord(1))
		print("here")
			#bus.write_byte(address,int(ord(j[0])))
		#	time.sleep(0)	
	# loop over the detected barcodes
	
	j1 ='5'
	j2 ='2'
	bus.write_byte(address,int(ord(j1)))
	
	for barcode in barcodes:
		# extract the bounding box location of the barcode and draw
		# the bounding box surrounding the barcode on the image
		bus.write_byte(address, int(ord(j1)))
		(x, y, w, h) = barcode.rect
		print(h,w)
		time.sleep(1)
	    	if (abs(w-h)<=2):
      			print("Nearly Correct Height")
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		# the barcode data is a bytes object so if we want to draw it
		# on our output image we need to convert it to a string first
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		#print(barcodeData)
		loc = barcodeData.split('|')
		xy = loc[0]
		print(xy[5:8])
		print(xy[10:13])
		#x =xy[0]
		#y = xy[1]
		#print(']n',x,y)

		# draw the barcode data and barcode type on the image
		text = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frame, text, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		# if the barcode text is currently not in our CSV file, write
		# the timestamp + barcode to disk and update the set
		if barcodeData not in found:
			csv.write("{},{}\n".format(datetime.datetime.now(),
				barcodeData))
			csv.flush()
			found.add(barcodeData)

	# show the output frame
	cv2.imshow("Barcode Scanner", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# close the output CSV file do a bit of cleanup
print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()
