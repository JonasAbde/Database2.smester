from db_connection import connect

def update_maling():
    try:
        connection = connect()
        cursor = connection.cursor()

        m_id = input("Indtast m_id for den måling, du vil opdatere: ")
        temp = input("Indtast ny temperatur: ")
        tryk = input("Indtast nyt tryk: ")

        cursor.execute("UPDATE measures SET temp = %s, tryk = %s, ts_measure = NOW() WHERE m_id = %s", (temp, tryk, m_id))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Måling med m_id {m_id} opdateret!")
        else:
            print(f"Der blev ikke fundet nogen måling med m_id {m_id}")
        
    except Exception as e:
        print("Fejl ved opdatering af måling:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()
