import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("chcampos/ping")
    client.message_callback_add("chcampos/ping", on_message_from_ping)

def on_message_from_ping(client, userdata, message):
   print("Custom callback  - ping: "+message.payload.decode())
   num = int(message.payload.decode())
   num = num +1
   client.publish("chcampos/pong", num)

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()

    client.on_connect = on_connect
    client.connect(host="172.20.10.9", keepalive=60)

    client.loop_start()
    time.sleep(1)
    num = 0
    while True:
        #replace user with your USC username in all subscriptions
        pass

