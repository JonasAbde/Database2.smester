import machine
import time
import network
import umqtt.simple as mqtt

BROKER = "din_broker_ip"
EMNE = "robocar/batteri_spaending"

adc = machine.ADC(28)

def laes_spaending():
    raw = adc.read_u16()
    spaending = (raw / 65535) * 3.3 * 2
    return spaending

def wifi_forbind():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect('dit_ssid', 'dit_password')
    while not wlan.isconnected():
        time.sleep(1)

def send_spaending():
    client = mqtt.MQTTClient("robocar", BROKER)
    client.connect()
    while True:
        spaending = laes_spaending()
        client.publish(EMNE, str(spaending))
        time.sleep(10)

wifi_forbind()
send_spaending()
