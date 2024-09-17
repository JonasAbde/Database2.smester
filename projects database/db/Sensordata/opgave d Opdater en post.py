import psycopg2

try:
    # Opret forbindelsesstrengen til databasen
    connect_str = "dbname='sensordata' user='avnadmin' host='pg-2f37e134-empire1266.f.aivencloud.com' " + \
                  "password='AVNS_GEfpyamT7kd4de4fIwU' port='19276'"

    # Opret forbindelsen til databasen
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()

    # Opdater værdier for posten med m_id = 5
    query_update = """
    UPDATE measures
    SET temp = %s, tryk = %s, ts_measure = NOW()
    WHERE m_id = %s;
    """
    cursor.execute(query_update, (10.80, 3.4, 5))

    # Gem ændringerne til databasen
    conn.commit()

    print("Post with m_id = 5 has been successfully updated.")

    # Luk cursor og forbindelse
    cursor.close()
    conn.close()

except Exception as e:
    print("Failed to update post with m_id = 5")
    print(e)
