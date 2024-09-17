from db_connection import connect

def delete_maling():
    try:
        connection = connect()
        cursor = connection.cursor()

        m_id = input("Indtast m_id for den måling, du vil slette: ")

        cursor.execute("DELETE FROM measures WHERE m_id = %s", (m_id,))
        connection.commit()

        if cursor.rowcount > 0:
            print(f"Måling med m_id {m_id} slettet!")
        else:
            print(f"Der blev ikke fundet nogen måling med m_id {m_id}")
        
    except Exception as e:
        print("Fejl ved sletning af måling:", e)
    finally:
        if connection:
            cursor.close()
            connection.close()
