import psycopg2

try:
    # Opret forbindelsesstrengen til databasen
    connect_str = "dbname='sensordata' user='avnadmin' host='pg-2f37e134-empire1266.f.aivencloud.com' " + \
                  "password='AVNS_GEfpyamT7kd4de4fIwU' port='19276'"

    # Opret forbindelsen til databasen
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    # Udfør en SQL-forespørgsel for at hente alle data fra measures-tabellen
    cursor.execute("SELECT * FROM measures;")
    
    # Hent alle resultater
    rows = cursor.fetchall()

    # Udskriv alle resultaterne
    for row in rows:
        print(f"m_id: {row[0]}, temp: {row[1]}, tryk: {row[2]}, ts_measure: {row[3]}")

    # Luk cursor og forbindelse
    cursor.close()
    conn.close()

except Exception as e:
    print("Can't connect. Invalid dbname, user or password")
    print(e)
