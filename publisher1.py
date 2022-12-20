import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")


def main():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("broker.emqx.io", 1883, 60)
    client.publish('raspberry/topic', payload="Sharzerot 1 e prazen", qos=0, retain=False)
    client.loop_forever()


if __name__ == "__main__":
    main()
