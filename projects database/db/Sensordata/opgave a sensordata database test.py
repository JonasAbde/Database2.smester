import psycopg2

# Forespørgsel til databasen for at hente temperatur, tryk og tidsstempel
query = ("""SELECT temp, tryk, ts_measure FROM measures""")

try:
    # Opret forbindelse til PostgreSQL-databasen
    connection = psycopg2.connect(
        user="avnadmin",
        password="AVNS_GEfpyamT7kd4de4fIwU",
        host="pg-2f37e134-empire1266.f.aivencloud.com",
        port="19276",
        database="sensordata"
    )

    # Opret en cursor til at udføre SQL-forespørgsler
    cursorA = connection.cursor()

    # Udfør SQL-forespørgslen
    cursorA.execute(query)

    # Hent alle resultater fra forespørgslen
    results = cursorA.fetchall()

    # Udskriv resultaterne
    for row in results:
        print(f"Temperatur: {row[0]}, Tryk: {row[1]}, Måletidspunkt: {row[2]}")

except (Exception, psycopg2.Error) as error:
    print("Failed to execute", error)

finally:
    # Lukker databaseforbindelsen
    if connection:
        cursorA.close()
        connection.close()
        print("PostgreSQL connection is closed")
