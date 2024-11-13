import psycopg2

def check_database():
    # Connect to the database
    conn = psycopg2.connect('postgres://avnadmin:AVNS_GEfpyamT7kd4de4fIwU@pg-2f37e134-empire1266.f.aivencloud.com:19276/Scoreboard?sslmode=require')
    cur = conn.cursor()

    # Execute the query to retrieve data
    cur.execute("SELECT * FROM game_log ORDER BY game_timestamp DESC LIMIT 10;")
    rows = cur.fetchall()

    # Print the data
    print("Latest game logs:")
    for row in rows:
        print(f"Game ID: {row[0]}, Player: {row[1]}, Sequence: {row[2]}, Score: {row[3]}, Timestamp: {row[4]}")

    # Close the database connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    check_database()
