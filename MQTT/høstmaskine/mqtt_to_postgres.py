import paho.mqtt.client as mqtt
import psycopg2
from psycopg2 import sql

# Opret forbindelse til PostgreSQL på Aiven
conn = psycopg2.connect(
    dbname="mqtt test",  # Den database du bruger på Aiven
    user="avnadmin",  # Brugernavn fra Aiven-konfiguration
    password="AVNS_GEfpyamT7kd4de4fIwU",  # Indsæt den adgangskode, du har fra Aiven
    host="pg-2f37e134-empire1266.f.aivencloud.com",  # Host fra din Aiven-server
    port="19276",  # Port fra din Aiven-server
    sslmode="require"  # SSL-forbindelse er påkrævet for Aiven
)
cursor = conn.cursor()

# Callback-funktion, der gemmer beskeder i databasen
def on_message(client, userdata, msg):
    print(f"Modtaget besked: {msg.payload.decode()} på emnet {msg.topic}")

    # SQL-spørring for at indsætte besked i tabellen i 'public' skemaet
    insert_query = sql.SQL(
        "INSERT INTO public.mqtt_messages (topic, payload) VALUES (%s, %s)"
    )
    
    # Udfør SQL-spørringen
    cursor.execute(insert_query, (msg.topic, msg.payload.decode()))

    # Gem ændringerne i databasen
    conn.commit()

# Opret MQTT-klient og tilknyt callback-funktionen
client = mqtt.Client()
client.on_message = on_message

# Opret forbindelse til MQTT broker og abonner på emnet 'trek/22/test'
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("trek/22/test")

# Hold klienten kørende for at modtage beskeder
client.loop_forever()

# Luk databaseforbindelsen, når du er færdig
conn.close()
