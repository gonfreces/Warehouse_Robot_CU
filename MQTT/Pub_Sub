import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt

#MQTT_SERVER = "10.201.73.61"
#MQTT_PATH = "1"

class mq_pub:
        def __init__(self, pat, ser, ms):
                self.path = pat
                self.serv = ser
                self.msg = ms

        def pub_me(self):
                publish.single(self.path,self.msg,hostname=self.serv)
                #publish.single(MQTT_PATH, "Hello PI!", hostname=MQTT_SERVER)


q1 = mq_pub("1", "10.201.73.61", "Hello Master PI")
q1.pub_me()
print("published")
q2 = mq_pub("1", "10.201.73.61", "stop")
q2.pub_me()
print("stopping")
print("subscribing")
pal = " "
p1=" "
MQTT_SERVER = "localhost"
MQTT_PATH_1 = "1" #ie.path
t ="Hello Pallet PI"
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
		print("checked pallet here")
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
client.loop_forever()

time.sleep(2)


while 1:
	print("i am pallet",pal)
	time.sleep(2)
