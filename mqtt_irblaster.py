import paho.mqtt.client as mqtt
import led_control as led
import mqtt_config as mqtt_conf

def on_connect(client, userdata, flags, rc):
    if(rc != 0):
        print("ON_CONNECT failed with error code: " + rc)
        exit()
    client.subscribe(mqtt_conf.BROKER_TOPIC, 0)

def on_message(client, userdata, msg):
    payload = str(msg.payload.decode("utf-8"))
    print("Received payload: " + str(payload))
    if(payload == "on"):
        led.led_on()
    elif(payload == "off"):
        led.led_off()

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to ", str(mid))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_subscribe = on_subscribe

client.username_pw_set(mqtt_conf.MQTT_BROKER_USERNAME, mqtt_conf.MQTT_BROKER_PASSWORD)
client.connect(mqtt_conf.BROKER_IP, mqtt_conf.BROKER_PORT, 60)

client.loop_forever()