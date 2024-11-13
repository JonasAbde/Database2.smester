import socket
import time

# Opret forbindelse til serveren
HOST = '10.120.0.18'
PORT = 5005

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        # Modtager sekvensen fra serveren
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
        
        # Behandl sekvensen som en liste af farver
        sequence = eval(data)
        print("Modtaget sekvens:", sequence)

        # Spilleren forsøger at efterligne sekvensen
        # Her kan du opdatere player_input til at læse input fra spilleren, hvis nødvendigt
        player_input = sequence  # For test antages korrekt input

        # Sender spillerens sekvens tilbage til serveren
        s.sendall(str(player_input).encode())

        # Modtager feedback fra serveren
        feedback = s.recv(1024).decode()
        status, score = feedback.split(',')

        if status == "correct":
            print(f"Sekvensen var korrekt! Din score er nu: {score}")
        elif status == "incorrect":
            print(f"Sekvensen var forkert. Spillet er slut. Din endelige score var: {score}")
            break  # Afslut spillet, hvis sekvensen er forkert

        time.sleep(2)
