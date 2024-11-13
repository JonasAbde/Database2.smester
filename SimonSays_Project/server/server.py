import socket
import random
import time
import psycopg2
import threading

# Server configuration
HOST = '10.120.0.18'
PORT = 5005

# Database connection setup
conn = psycopg2.connect('postgres://avnadmin:AVNS_GEfpyamT7kd4de4fIwU@pg-2f37e134-empire1266.f.aivencloud.com:19276/Scoreboard?sslmode=require')
cur = conn.cursor()

# Create necessary tables if they don’t already exist
cur.execute("""
CREATE TABLE IF NOT EXISTS game_log (
    game_id SERIAL PRIMARY KEY,
    player_name VARCHAR(50),
    sequence VARCHAR(255),
    score INT,
    game_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()

# Helper function to save game data to the database
def save_game_log(player_name, sequence, score):
    try:
        print(f"[DEBUG] Saving to database: player_name={player_name}, sequence={sequence}, score={score}")
        cur.execute(
            "INSERT INTO game_log (player_name, sequence, score) VALUES (%s, %s, %s)",
            (player_name, str(sequence), score)
        )
        conn.commit()
        print("Game log saved successfully.")
    except Exception as e:
        print("Error saving game log:", e)
        conn.rollback()

# Flag to control game state
game_running = True

# Function to listen for server input to manually end the game
def listen_for_end_command():
    global game_running
    while game_running:
        command = input("Indtast 'slut' for at afslutte spillet: ")
        if command.lower() == "slut":
            game_running = False
            print("Spillet afsluttes manuelt.")

# Start a separate thread to listen for the "slut" command
input_thread = threading.Thread(target=listen_for_end_command)
input_thread.start()

# Start the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print("Server venter på spillere...")

    # Connect to Player 1
    player1_socket, player1_address = server_socket.accept()
    print(f"Spiller 1 forbundet fra {player1_address}")

    # Connect to Player 2
    player2_socket, player2_address = server_socket.accept()
    print(f"Spiller 2 forbundet fra {player2_address}")

    while game_running:
        # Start a new sequence for the game
        sequence = []
        round_active = True
        scores = {"Spiller 1": 0, "Spiller 2": 0}

        while round_active and game_running:
            # Add a new color to the sequence
            new_color = random.choice(["red", "green", "blue", "yellow"])
            sequence.append(new_color)
            print("[DEBUG] Ny sekvens genereret:", sequence)

            # Send sequence to both players
            for player_socket in (player1_socket, player2_socket):
                player_socket.sendall(str(sequence).encode())

            # Get each player’s input
            for player_socket, player_name in zip((player1_socket, player2_socket), ("Spiller 1", "Spiller 2")):
                player_input = player_socket.recv(1024).decode()
                player_input = eval(player_input)

                if player_input == sequence:
                    feedback = "correct"
                    scores[player_name] += 1  # Increment the player's score
                    player_socket.sendall(f"{feedback},{scores[player_name]}".encode())
                else:
                    feedback = "incorrect"
                    player_socket.sendall(f"{feedback},{scores[player_name]}".encode())
                    print(f"{player_name} tabte spillet.")
                    
                    # Log the final sequence and score to the database
                    save_game_log(player_name, sequence, scores[player_name])
                    
                    round_active = False
                    break

            # Pause mellem runder
            time.sleep(1)

        if not game_running:
            # If the game was stopped manually, log the scores for both players
            print("[DEBUG] Server afsluttes manuelt. Gemmer scores.")
            save_game_log("Spiller 1", sequence, scores["Spiller 1"])
            save_game_log("Spiller 2", sequence, scores["Spiller 2"])
            break  # Exit the game loop if "slut" command was given

        # Game over message to players
        for player_socket in (player1_socket, player2_socket):
            player_socket.sendall("game_over".encode())

        # Wait for players to signal readiness for a new game
        for player_socket, player_name in zip((player1_socket, player2_socket), ("Spiller 1", "Spiller 2")):
            confirmation = player_socket.recv(1024).decode()
            if confirmation.lower() == "ready":
                print(f"{player_name} er klar til et nyt spil.")

        print("Starter et nyt spil...")

# Close database connection
cur.close()
conn.close()

# Close player connections
player1_socket.close()
player2_socket.close()

print("Serveren er afsluttet.")
