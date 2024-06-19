import json
# Codice per la connessione e la configurazione del client MQTT
# Definisci le funzioni di callback per la gestione degli eventi MQTT
def on_connect(client, userdata, flags, rc): #properties
    if rc == 0:
        print("Connessione al broker MQTT riuscita")
    else:
        print("Connessione al broker MQTT fallita, codice di ritorno:", rc)

def on_publish(client, userdata, mid): #, reason_code, properties
    print(f"Messaggio pubblicato con successo, ID del messaggio: {mid}")

    
def convert_byte_string_to_json(byte_string):
    try:
        # Decode the byte string using UTF-8 encoding (common for JSON)
        json_string = byte_string.decode('utf-8')
        # Use json.loads to parse the JSON string into a Python object
        return json.loads(json_string)
    except (UnicodeDecodeError, json.JSONDecodeError) as e:
        raise ValueError(f"Error parsing JSON data: {e}") from e

    
def acm_sensor_callback(client, userdata, message):
    print("acm_sensor_callback")
    python_object = convert_byte_string_to_json(message.payload)
    print(python_object)

def gyr_sensor_callback(client, userdata, message):
    print("gyr_sensor_callback")
    python_object = convert_byte_string_to_json(message.payload)
    print(python_object)


def mgt_sensor_callback(client, userdata, message):
    print("mgt_sensor_callback")
    python_object = convert_byte_string_to_json(message.payload)
    print(python_object)
    
def gps_sensor_callback(client, userdata, message):
    print("gps_sensor_callback")
    python_object = convert_byte_string_to_json(message.payload)
    print(python_object)

def als_sensor_callback(client, userdata, message):
    print("als_sensor_callback")
    python_object = convert_byte_string_to_json(message.payload)
    print(python_object)
    