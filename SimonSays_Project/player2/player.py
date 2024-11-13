import socket
import time
from button_handler import get_pressed_button  # Importer knapfunktioner

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
        
        sequence = eval(data)
        print("Modtaget sekvens:", sequence)

        # Spilleren trykker på knapper for at vælge farver
        player_input = []
        for _ in range(len(sequence)):
            selected_color = None
            while not selected_color:
                selected_color = get_pressed_button()  # Få farven på den trykkede knap
            player_input.append(selected_color)
            print(f"Spiller valgte: {selected_color}")
            time.sleep(0.5)  # Lille forsinkelse for at undgå gentagelser

        # Sender spillerens sekvens tilbage til serveren
        s.sendall(str(player_input).encode())

        # Modtager feedback fra serveren
        feedback = s.recv(1024).decode()
        if feedback == "correct":
            print("Sekvensen var korrekt!")
        elif feedback == "incorrect":
            print("Sekvensen var forkert. Spillet er slut.")
            break  # Afslut spillet, hvis sekvensen er forkert

        time.sleep(2)
