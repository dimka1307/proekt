import paho.mqtt.client as mqtt
import time
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def main(sharzer1,sharzer2,sharzer3,produkti):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)
    client.publish('raspberry/topic', payload=str(sharzer1) + " " + str(sharzer2) + " " + str(sharzer3), qos=0, retain=False)
    client.publish('raspberry/topic', payload=current_time + " " + str(produkti), qos=0, retain=False)
    client.loop_forever()


if __name__ == "__main__":
    main()
