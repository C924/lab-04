import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("chcampos/ping")
    client.message_callback_add("chcampos/pong", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
   print("Message received  - pong: "+message.payload.decode())
   num = int(message.payload.decode())
   new_num = num + 1
   time.sleep(1)
   client.publish("chcampos/ping", new_num)
   print("Message sent", new_num)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("172.20.10.7", port = 11000, keepalive=60)
    client.loop_forever()


