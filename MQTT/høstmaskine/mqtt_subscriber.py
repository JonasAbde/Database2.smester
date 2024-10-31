import paho.mqtt.client as mqtt

# Callback-funktion, der kaldes, når en besked modtages
def on_message(client, userdata, msg):
    print(f"Modtaget besked: {msg.payload.decode()} på emnet {msg.topic}")
    # Log beskeden til en fil
    with open("mqtt_log.txt", "a") as log_file:
        log_file.write(f"{msg.topic}: {msg.payload.decode()}\n")

# Opret en MQTT-klient og tilknyt callback-funktionen
client = mqtt.Client()
client.on_message = on_message

# Opret forbindelse til broker og abonner på emnet 'trek/22/test'
client.connect("test.mosquitto.org", 1883, 60)
client.subscribe("trek/22/test")

# Hold klienten kørende for at modtage beskeder
client.loop_forever()
