import paho.mqtt.client as mqtt
import time
pal = " "
p1=" "
MQTT_SERVER = "localhost"
MQTT_PATH_1 = "1" #ie.path
t ="Hello PI"
client = mqtt.Client()
#client.loop_start()
#class mq_sub:

	#p1 = 0
#	def __init__(self, path, text):
		#MQTT_SERVER = "localhost"
		#MQTT_PATH_1 = "1" #ie.path
#		self.p = path
#		self.t = text
def on_connect(client,userdata, flags, rc):
	print("connected with result code"+str(rc))
	#client.subscribe(self.path)
       	client.subscribe(MQTT_PATH_1)

def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.payload))
	p1 = str(msg.payload)
	global pal
#	def reply(self):
	if p1 == t:
		print("checked")
		pal = p1
#"hi"
		print(pal)
	if  p1 == "stop":
		client.disconnect()
		#pal = "sgs"
		#break

#client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883,60)
	#client.connect("localhost",1883,60)
print("fcsfs // ", pal) #,str(msg.payload))
time.sleep(2)
client.loop_forever()

while 1:
	print("12",pal)
	time.sleep(2)
