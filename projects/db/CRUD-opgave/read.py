from db_connection import connect

def read_maling():
    try:
        connection = connect()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM measures")
        rows = cursor.fetchall()

        for row in rows:
            print(f"m_id: {row[0]}, temp: {row[1]}, tryk: {row[2]}, ts_measure: {row[3]}")
        
    except Exception as e:
        print("Fejl ved læsning af måling:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()
