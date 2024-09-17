import psycopg2

try:
    # Opret forbindelsesstrengen til databasen
    connect_str = "dbname='sensordata' user='avnadmin' host='pg-2f37e134-empire1266.f.aivencloud.com' " + \
                  "password='AVNS_GEfpyamT7kd4de4fIwU' port='19276'"

    # Opret forbindelsen til databasen
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    # Indsæt en ny post med næste ledige m_id og værdierne temp, tryk, ts_measure
    query_insert = """
    INSERT INTO measures (temp, tryk, ts_measure)
    VALUES (%s, %s, NOW());
    """
    cursor.execute(query_insert, (19.34, 1.2))

    # Gem ændringerne til databasen
    conn.commit()

    print("Post successfully inserted into the database.")

    # Luk cursor og forbindelse
    cursor.close()
    conn.close()

except Exception as e:
    print("Failed to insert post into database")
    print(e)
