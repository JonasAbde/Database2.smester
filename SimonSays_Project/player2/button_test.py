# button_test.py

from machine import Pin
import time

# Konfigurer GPIO-pins
button_pin = 0  # GPIO-pin til den røde knap
led_pin = 1     # GPIO-pin til den indbyggede LED

# Opsætning af knap og LED
button = Pin(button_pin, Pin.IN, Pin.PULL_DOWN)
led = Pin(led_pin, Pin.OUT)

print("Tryk på den røde knap for at teste...")

while True:
    if button.value():
        print("Rød knap trykket!")
        led.on()  # Tænd LED'en
        time.sleep(0.5)  # Debounce-forsinkelse
    else:
        led.off()  # Sluk LED'en
    time.sleep(0.1)  # Polling-interval
