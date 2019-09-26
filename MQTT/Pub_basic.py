import paho.mqtt.publish as publish


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


q1 = mq_pub("1", "10.201.73.61", "Hello PI")
q1.pub_me()
