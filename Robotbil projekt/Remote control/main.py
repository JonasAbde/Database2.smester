# Filename: main.py

import network
import socket
import motor
import time
import select

# WiFi-konfiguration
ssid = 'WifiD010'        # Udskift med din WiFi SSID
password = '99adh14ah'   # Udskift med din WiFi-adgangskode

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

# Opsæt UDP-server
udp_port = 5005
udp_addr = socket.getaddrinfo('0.0.0.0', udp_port)[0][-1]
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(udp_addr)
udp_socket.setblocking(False)  # Ikke-blokerende socket

print(f"UDP-server lytter på port {udp_port}...")

# Opsæt HTTP-server
http_port = 80
http_addr = socket.getaddrinfo('0.0.0.0', http_port)[0][-1]
http_socket = socket.socket()
http_socket.bind(http_addr)
http_socket.listen(1)
http_socket.setblocking(False)  # Ikke-blokerende socket

print(f"HTTP-server lytter på port {http_port}...")

# Globale variabler for motorhastigheder og kalibrering
current_speed_left = 0
current_speed_right = 0
boost_active = False  # Sporer boost-status

# Kalibreringsfaktorer
CALIBRATION_LEFT = 1.0     # Juster denne værdi baseret på dine tests
CALIBRATION_RIGHT = 1.05   # Øget for at kompensere for veering til højre

# Definer bilens maksimale hastighed i km/t (fra din måling)
MAX_SPEED_KMH = 7.2  # Opdater denne værdi baseret på dine målinger

# Hovedløkke til at håndtere indkommende UDP-kommandoer og HTTP-anmodninger
while True:
    try:
        # Brug select til at håndtere flere sockets
        readable, _, _ = select.select([udp_socket, http_socket], [], [], 0.01)
        for s in readable:
            if s is udp_socket:
                # Håndter UDP-kommandoer
                data, client_addr = udp_socket.recvfrom(1024)
                request = data.decode('utf-8')
                print(f'Modtaget kommando: {request} fra {client_addr}')

                # Opdel kommandoen i handling og motorhastigheder
                if ':' in request:
                    action, speed_left_str, speed_right_str = request.split(':')
                    speed_left = float(speed_left_str)
                    speed_right = float(speed_right_str)
                else:
                    action = request
                    speed_left = 50.0  # Standardhastighed
                    speed_right = 50.0  # Standardhastighed

                # Håndter boost-kommandoer
                if action == 'BOOST_ON':
                    print("Boost aktiveret")
                    boost_active = True
                elif action == 'BOOST_OFF':
                    print("Boost deaktiveret")
                    boost_active = False

                # Håndter bevægelseskommandoer med specificerede hastigheder
                elif action == 'MOVE':
                    if boost_active:
                        # Forøg hastigheden med 20%, op til maksimalt 100%
                        speed_left = min(speed_left * 1.2, 100)
                        speed_right = min(speed_right * 1.2, 100)

                    # Anvend kalibrering
                    speed_left *= CALIBRATION_LEFT
                    speed_right *= CALIBRATION_RIGHT

                    # Sikr hastighedsgrænser
                    speed_left = max(-100, min(100, speed_left))
                    speed_right = max(-100, min(100, speed_right))

                    print(f"Kører med venstre hastighed: {speed_left}% og højre hastighed: {speed_right}%")
                    motor.move(speed_left, speed_right)
                    current_speed_left = speed_left  # Opdater globale hastighedsvariabler
                    current_speed_right = speed_right
                elif action == 'STOP':
                    print("Stopper motorer")
                    motor.stop()
                    current_speed_left = 0
                    current_speed_right = 0
                else:
                    print(f"Ugyldig kommando: {request}")

            elif s is http_socket:
                # Håndter HTTP-anmodninger
                conn, addr = http_socket.accept()
                conn.settimeout(3.0)  # Valgfri timeout
                try:
                    request = conn.recv(1024)
                    request = str(request)
                    print(f'HTTP-anmodning fra {addr}: {request}')

                    # Læs HTML-filen
                    with open('index.html', 'r') as f:
                        html_content = f.read()

                    # Beregn hastighed og retning for venstre motor
                    if current_speed_left > 0:
                        direction_left = "Fremad"
                    elif current_speed_left < 0:
                        direction_left = "Bagud"
                    else:
                        direction_left = "Stoppet"

                    speed_left_kmh = (abs(current_speed_left) / 100) * MAX_SPEED_KMH

                    # Beregn hastighed og retning for højre motor
                    if current_speed_right > 0:
                        direction_right = "Fremad"
                    elif current_speed_right < 0:
                        direction_right = "Bagud"
                    else:
                        direction_right = "Stoppet"

                    speed_right_kmh = (abs(current_speed_right) / 100) * MAX_SPEED_KMH

                    # Erstat pladsholdere i HTML
                    html_content = html_content.replace('{speed_left_kmh}', f"{speed_left_kmh:.2f}")
                    html_content = html_content.replace('{speed_right_kmh}', f"{speed_right_kmh:.2f}")
                    html_content = html_content.replace('{direction_left}', direction_left)
                    html_content = html_content.replace('{direction_right}', direction_right)

                    # Forbered og send HTTP-responsen
                    response = 'HTTP/1.1 200 OK\n\n' + html_content
                    conn.send(response.encode('utf-8'))
                except Exception as e:
                    print(f"Fejl ved håndtering af HTTP-anmodning: {e}")
                finally:
                    conn.close()

    except Exception as e:
        print(f"Fejl: {e}")

    # Fjern eller reducer sleep for at øge responsiviteten
    # time.sleep(0.01)
