from machine import Pin
import time

# Konfigurer GPIO-pins til knapper og LED'er
button_pin_red = 0     # GPIO-pin til den røde knap
button_pin_blue = 8    # GPIO-pin til den blå knap
button_pin_green = 19  # GPIO-pin til den grønne knap
button_pin_yellow = 28 # GPIO-pin til den gule knap
led_pin_red = 1        # GPIO-pin til den røde LED
led_pin_blue = 9       # GPIO-pin til den blå LED
led_pin_green = 18     # GPIO-pin til den grønne LED
led_pin_yellow = 27    # GPIO-pin til den gule LED

# Opsætning af knapper og LED'er med Pull-up modstand
button_red = Pin(button_pin_red, Pin.IN, Pin.PULL_UP)
button_blue = Pin(button_pin_blue, Pin.IN, Pin.PULL_UP)
button_green = Pin(button_pin_green, Pin.IN, Pin.PULL_UP)
button_yellow = Pin(button_pin_yellow, Pin.IN, Pin.PULL_UP)

led_red = Pin(led_pin_red, Pin.OUT)
led_blue = Pin(led_pin_blue, Pin.OUT)
led_green = Pin(led_pin_green, Pin.OUT)
led_yellow = Pin(led_pin_yellow, Pin.OUT)

# Variabler til at holde knapstatus
button_pressed_red = False
button_pressed_blue = False
button_pressed_green = False
button_pressed_yellow = False

# Callback-funktioner for knapperne
def button_callback_red(pin):
    global button_pressed_red
    if pin.value() == 0:
        button_pressed_red = True
        print("Rød knap trykket!")
        led_red.on()

def button_callback_blue(pin):
    global button_pressed_blue
    if pin.value() == 0:
        button_pressed_blue = True
        print("Blå knap trykket!")
        led_blue.on()

def button_callback_green(pin):
    global button_pressed_green
    if pin.value() == 0:
        button_pressed_green = True
        print("Grøn knap trykket!")
        led_green.on()

def button_callback_yellow(pin):
    global button_pressed_yellow
    if pin.value() == 0:
        button_pressed_yellow = True
        print("Gul knap trykket!")
        led_yellow.on()

# Opret interrupt til knapperne (registrerer når pin går fra høj til lav)
button_red.irq(trigger=Pin.IRQ_FALLING, handler=button_callback_red)
button_blue.irq(trigger=Pin.IRQ_FALLING, handler=button_callback_blue)
button_green.irq(trigger=Pin.IRQ_FALLING, handler=button_callback_green)
button_yellow.irq(trigger=Pin.IRQ_FALLING, handler=button_callback_yellow)

# Loop til at nulstille knapper og slukke LED'er
while True:
    if button_pressed_red:
        time.sleep(0.2)  # Debounce
        button_pressed_red = False
        led_red.off()

    if button_pressed_blue:
        time.sleep(0.2)
        button_pressed_blue = False
        led_blue.off()

    if button_pressed_green:
        time.sleep(0.2)
        button_pressed_green = False
        led_green.off()

    if button_pressed_yellow:
        time.sleep(0.2)
        button_pressed_yellow = False
        led_yellow.off()
