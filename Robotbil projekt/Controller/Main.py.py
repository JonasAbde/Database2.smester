import network
import socket
import motor
import time

# WiFi-konfiguration
ssid = 'ITEK 2nd'
password = '2nd_Semester_E24a'

# Opret forbindelse til WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

print("Forbinder til WiFi-netværket...")

timeout = 10
while not wlan.isconnected() and timeout > 0:
    print("Forsøger at forbinde...")
    time.sleep(1)
    timeout -= 1

if wlan.isconnected():
    print("Forbundet til WiFi!")
    print(f"IP-adresse: {wlan.ifconfig()[0]}")
else:
    print("Kunne ikke oprette forbindelse til WiFi.")

# Opsætning af en UDP-server
udp_port = 5005
addr = socket.getaddrinfo('0.0.0.0', udp_port)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)

print(f"UDP server lytter på port {udp_port}...")

# Main-loop for at håndtere indkommende UDP-kommandoer
while True:
    try:
        data, client_addr = s.recvfrom(1024)
        request = data.decode('utf-8')
        print(f'Modtaget kommando: {request} fra {client_addr}')

        # Split kommandoen i action og motor hastigheder
        if ':' in request:
            action, speed_left_str, speed_right_str = request.split(':')
            speed_left = int(float(speed_left_str))  # Konverter til float først, og derefter til int
            speed_right = int(float(speed_right_str))  # Samme her
        else:
            action = request
            speed_left = 50  # Standard hastighed
            speed_right = 50  # Standard hastighed

        # Håndter boost-kommandoer
        if action == 'BOOST_ON':
            print("Boost aktiveret")
        elif action == 'BOOST_OFF':
            print("Boost deaktiveret")

        # Håndter bevægelseskommandoer med de specificerede hastigheder
        elif action == 'MOVE':
            print(f"Kører med venstre hastighed: {speed_left}% og højre hastighed: {speed_right}%")
            motor.move(speed_left, speed_right)
        elif action == 'STOP':
            print("Stopper motorer")
            motor.stop()

        else:
            print(f"Ugyldig kommando: {request}")
    except Exception as e:
        print(f"Fejl ved modtagelse af kommando: {e}")

    time.sleep(0.05)