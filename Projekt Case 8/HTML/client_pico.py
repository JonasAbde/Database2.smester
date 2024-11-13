import network
import socket
import time
import random
from machine import Pin

# WiFi-indstillinger
SSID = 'YOUR_WIFI_SSID'
PASSWORD = 'YOUR_WIFI_PASSWORD'

# Konfiguration af LED'er
led_red = Pin(15, Pin.OUT)
led_green = Pin(14, Pin.OUT)
led_blue = Pin(13, Pin.OUT)
led_yellow = Pin(12, Pin.OUT)

# Opsætning af WiFi og UDP
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while not wlan.isconnected():
    time.sleep(1)
print("Tilsluttet til WiFi")

# Modtagelse af sekvenser
while True:
    data, addr = udp_socket.recvfrom(1024)
    sequence = data.decode().split(",")
    print("Modtaget sekvens:", sequence)

    # Vis sekvensen på LED'er
    for color in sequence:
        if color == "red":
            led_red.on()
            time.sleep(0.5)
            led_red.off()
        elif color == "green":
            led_green.on()
            time.sleep(0.5)
            led_green.off()
        elif color == "blue":
            led_blue.on()
            time.sleep(0.5)
            led_blue.off()
        elif color == "yellow":
            led_yellow.on()
            time.sleep(0.5)
            led_yellow.off()
