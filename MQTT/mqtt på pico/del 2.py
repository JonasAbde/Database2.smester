import machine
import time
import network
import umqtt.simple as mqtt

BROKER = "din_broker_ip"
EMNE_LED = "trek/22/led"

led = machine.Pin(25, machine.Pin.OUT)

def wifi_forbind():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('dit_ssid', 'dit_password')
    while not wlan.isconnected():
        time.sleep(1)

def modtag_besked(emne, besked):
    if besked == b'ON':
        led.value(1)
    elif besked == b'OFF':
        led.value(0)

def lyt_mqtt():
    client = mqtt.MQTTClient("led_styring", BROKER)
    client.set_callback(modtag_besked)
    client.connect()
    client.subscribe(EMNE_LED)
    while True:
        client.check_msg()
        time.sleep(1)

wifi_forbind()
lyt_mqtt()
