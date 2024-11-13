# db_helper.py
import psycopg2

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

# Helper function to save game data
def save_game_log(player_name, sequence, score):
    try:
        print(f"[DEBUG] Attempting to save to database: player_name={player_name}, sequence={sequence}, score={score}")
        cur.execute(
            "INSERT INTO game_log (player_name, sequence, score) VALUES (%s, %s, %s)",
            (player_name, str(sequence), score)
        )
        conn.commit()
        print("Game log saved successfully.")
    except Exception as e:
        print("Error saving game log:", e)
        conn.rollback()  # Rollback in case of error

# Function to test database insertion
def test_database_insertion():
    # Insert a test record
    save_game_log("Test Player", ["red", "green", "blue"], 3)
    
    # Retrieve the last 5 records to verify the insertion
    try:
        cur.execute("SELECT * FROM game_log ORDER BY game_timestamp DESC LIMIT 5;")
        rows = cur.fetchall()
        print("Latest game logs:")
        for row in rows:
            print(f"Game ID: {row[0]}, Player: {row[1]}, Sequence: {row[2]}, Score: {row[3]}, Timestamp: {row[4]}")
    except Exception as e:
        print("Error retrieving game logs:", e)

# Close connections when the module is not in use anymore
def close_connection():
    cur.close()
    conn.close()
    print("Database connection closed.")

if __name__ == "__main__":
    test_database_insertion()
    close_connection()
