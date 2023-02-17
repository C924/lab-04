import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("chcampos/pong")
    client.message_callback_add("chcampos/pong", on_message_from_pong)

def on_message_from_pong(client, userdata, message):
   print("Custom callback  - pong: "+message.payload.decode())
   num = int(message.payload.decode())
   num = num +1
   client.publish("chcampos/ping", num)

if __name__ == '__main__':
    #create a client object
    client = mqtt.Client()

    client.on_connect = on_connect
    client.connect(host="172.20.10.9", keepalive=60)

    client.loop_start()
    time.sleep(1)

    while True:
        #replace user with your USC username in all subscriptions
        pass

