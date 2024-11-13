from machine import Pin
import time

# Konfigurer GPIO-pins
button_pin = 0  # GPIO-pin til den røde knap
led_pin = 1     # GPIO-pin til den indbyggede LED

# Opsætning af knap og LED med Pull-up modstand
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
led = Pin(led_pin, Pin.OUT)

# Variabler til debounce og knapstatus
button_pressed = False
last_press_time = 0  # Holder styr på sidste tryktid

# Debounce delay i millisekunder
DEBOUNCE_DELAY = 200  # 200 ms

# Callback-funktion for knappen
def button_callback(pin):
    global button_pressed, last_press_time
    current_time = time.ticks_ms()  # Hent nuværende tid i millisekunder

    # Tjek om tiden siden sidste tryk er større end debounce-tiden
    if time.ticks_diff(current_time, last_press_time) > DEBOUNCE_DELAY:
        last_press_time = current_time  # Opdater sidste tryktid
        button_pressed = True
        print("Rød knap trykket!")  # Dette udskrives kun én gang pr. tryk
        led.on()  # Tænd LED

# Opret interrupt til knappen (registrerer når pin går fra høj til lav)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_callback)

# Loop til at nulstille knappen og slukke LED
while True:
    if button_pressed:
        time.sleep(0.2)  # Giv tid til at se LED lyse op
        button_pressed = False  # Nulstil variabel
        led.off()  # Sluk LED
