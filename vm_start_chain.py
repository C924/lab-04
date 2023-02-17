import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("chcampos/pong")
    client.message_callback_add("chcampos/ping", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
   print("Message received  - ping: "+message.payload.decode())
   num = int(message.payload.decode())
   new_num = num + 1
   client.publish("chcampos/pong", new_num)
   print("Message sent", new_num)

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("172.20.10.9", port = 1883, keepalive=60)
    client.loop_start()

    num = 0
    time.sleep(1)
    client.publish("chcampos/pong", num)
    print("Message sent",  num)

    while True:
        pass

