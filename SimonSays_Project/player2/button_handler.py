from machine import Pin
import time

# Konfigurer GPIO-pins som input til knapper
red_button = Pin(0, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(1, Pin.IN, Pin.PULL_DOWN)
blue_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
yellow_button = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Funktion til at tjekke hvilken knap der er trykket
def get_pressed_button():
    if red_button.value():
        return "red"
    elif green_button.value():
        return "green"
    elif blue_button.value():
        return "blue"
    elif yellow_button.value():
        return "yellow"
    return None
