import pygame
import socket
import time

# Initialiser pygame for at bruge Xbox-controlleren
pygame.init()
pygame.joystick.init()

# Tjek om Xbox-controlleren er tilsluttet
if pygame.joystick.get_count() == 0:
    print("Ingen Xbox-controller fundet.")
    exit()

# Tilslut Xbox-controlleren
controller = pygame.joystick.Joystick(0)
controller.init()

print("Xbox-controller tilsluttet via Bluetooth.")

# IP-adressen til din Raspberry Pi Pico W
PICO_IP = '10.120.0.15'  # Opdater dette med den korrekte IP-adresse fra Pico W
UDP_PORT = 5005  # Samme port som UDP-serveren på Pico W

# Opret en UDP-klient
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Funktion til at sende kommandoer via UDP med hastigheder for begge motorer
def send_command(command, speed_left, speed_right):
    try:
        message = f"{command}:{speed_left}:{speed_right}"  # Sender kommando + hastigheder for venstre og højre motor
        s.sendto(message.encode('utf-8'), (PICO_IP, UDP_PORT))
        print(f"Sendt: {message} til {PICO_IP}:{UDP_PORT}")
    except Exception as e:
        print(f"Fejl ved afsendelse af kommando: {e}")


boost_active = False  # Variabel til at holde styr på, om boost er aktiv
normal_speed = 55  # Normal hastighed
boost_speed = 95   # Boost hastighed

# Kontroller event-handling loop
while True:
    # Tjek for events (controller input)
    pygame.event.pump()

    # Læs D-pad (hat) position for fremad/baglæns og drejning
    dpad_x, dpad_y = controller.get_hat(0)  # Hent D-pad position

    # Tjek om A-knappen (boost) trykkes
    button_a = controller.get_button(0)

    # Juster hastigheden baseret på booststatus
    current_speed = boost_speed if boost_active else normal_speed

    # Hvis A-knappen trykkes ned, aktiver boost, ellers deaktiver det
    if button_a and not boost_active:
        send_command('BOOST_ON', current_speed, current_speed)
        boost_active = True
    elif not button_a and boost_active:
        send_command('BOOST_OFF', current_speed, current_speed)
        boost_active = False

    # Variabler til at justere venstre og højre motor
    speed_left = 0
    speed_right = 0

    # Kombineret bevægelse fremad/baglæns og drejning baseret på D-pad
    if dpad_y == 1:  # Pil op (fremad)
        speed_left = current_speed
        speed_right = current_speed
    elif dpad_y == -1:  # Pil ned (baglæns)
        speed_left = -current_speed
        speed_right = -current_speed

    # Juster for drejning (kombinér med fremad/baglæns bevægelse)
    if dpad_x == 1:  # Pil venstre (drej venstre)
        speed_left *= 0.6  # Sænk hastigheden på venstre motor for at dreje til venstre
    elif dpad_x == -1:  # Pil højre (drej højre)
        speed_right *= 0.6  # Sænk hastigheden på højre motor for at dreje til højre

    # Hvis både X og Y er nul (ingen input), stop motorerne
    if dpad_x == 0 and dpad_y == 0:
        send_command('STOP', 0, 0)
    else:
        # Send bevægelseskommandoen
        send_command('MOVE', speed_left, speed_right)

    # Debug-udskrivning for D-pad status
    print(f'D-pad position (X): {dpad_x}, (Y): {dpad_y}, Venstre hastighed = {speed_left}, Højre hastighed = {speed_right}, Boost: {boost_active}')

    time.sleep(0.1)
