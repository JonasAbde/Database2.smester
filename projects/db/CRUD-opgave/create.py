from db_connection import connect

def create_maling():
    try:
        connection = connect()
        cursor = connection.cursor()

        temp = input("Indtast temperatur: ")
        tryk = input("Indtast tryk: ")

        cursor.execute("INSERT INTO measures (temp, tryk, ts_measure) VALUES (%s, %s, NOW())", (temp, tryk))
        connection.commit()
        print("Måling oprettet!")
        
    except Exception as e:
        print("Fejl ved oprettelse af måling:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()
