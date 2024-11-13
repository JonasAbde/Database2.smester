import network
import socket
import time
from machine import Pin

# WiFi-konfiguration
SSID = "ITEK 2nd"
PASSWORD = "2nd_Semester_E24a"

# Server konfiguration (PC'ens IP-adresse og port)
HOST = '10.120.0.18'  # Skift til PC'ens IP-adresse
PORT = 5005

# WiFi-forbindelse
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    
    while not wlan.isconnected():
        print("Forbinder til WiFi...")
        time.sleep(1)
    
    print("Forbundet til WiFi:", wlan.ifconfig())

# Knap og LED-konfiguration
buttons = {
    "red": {"pin": 0, "led": 1},    # GPIO 0 for rød knap og GPIO 1 for rød LED
    "green": {"pin": 2, "led": 3},  # GPIO 2 for grøn knap og GPIO 3 for grøn LED
    "blue": {"pin": 4, "led": 5},   # GPIO 4 for blå knap og GPIO 5 for blå LED
    "yellow": {"pin": 6, "led": 7}  # GPIO 6 for gul knap og GPIO 7 for gul LED
}

# Initialiser knapper og LED'er
for color, pins in buttons.items():
    buttons[color]["button"] = Pin(pins["pin"], Pin.IN, Pin.PULL_UP)
    buttons[color]["led"] = Pin(pins["led"], Pin.OUT)
    buttons[color]["led"].off()  # Sluk alle LED'er i starten

# Forbind til WiFi
connect_to_wifi()

# Opret forbindelse til serveren
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        # Modtag sekvensen fra serveren
        data = s.recv(1024).decode()
        
        if data == "game_over":
            print("Spillet er slut.")
            # Vent på brugerens bekræftelse for at starte et nyt spil
            ready = input("Er du klar til et nyt spil? (skriv 'ready' for at starte): ")
            s.sendall(ready.encode())
            if ready.lower() != "ready":
                print("Afslutter spil.")
                break
            continue
        
        # Evaluér og udpak sekvensen
        sequence = eval(data)
        print("Modtaget sekvens:", sequence)

        # Vis sekvensen til spilleren med LED'er
        for color in sequence:
            if color in buttons:
                buttons[color]["led"].on()  # Tænd LED'en for den aktuelle farve
                time.sleep(0.5)  # Kort tid for at vise farven
                buttons[color]["led"].off()
                time.sleep(0.2)  # Kort pause mellem farver

        # Lyt efter spillerens sekvensinput uden at vente på hver enkelt tryk
        player_sequence = []
        print("Tryk på knapperne for at matche sekvensen.")
        
        while len(player_sequence) < len(sequence):
            for color, config in buttons.items():
                if config["button"].value() == 0:  # Knap trykket
                    print(f"Spiller trykkede på {color}.")
                    player_sequence.append(color)
                    time.sleep(0.3)  # Forsinkelse for at undgå dobbelt registrering

        # Send spillerens sekvens tilbage til serveren
        s.sendall(str(player_sequence).encode())

        # Modtag feedback fra serveren
        feedback = s.recv(1024).decode()
        if feedback == "correct":
            print("Sekvensen var korrekt!")
        elif feedback == "incorrect":
            print("Sekvensen var forkert. Spillet er slut.")
            break  # Afslut spillet, hvis sekvensen er forkert

        time.sleep(2)
finally:
    # Luk forbindelsen manuelt
    s.close()
    print("Forbindelse lukket.")
