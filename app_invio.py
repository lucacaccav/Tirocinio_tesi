import json
from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import mqtt_function as callback


app = Flask(__name__,static_folder='static')   
mqtt_client = mqtt.Client() #mqtt.CallbackAPIVersion.VERSION2
TOPIC = {"acm_sensor","gyr_sensor","mgt_sensor","gps_sensor","als_sensor"}


def init_mqtt_client():
    #mqtt_client.connect("localhost", 1883, 60)
    mqtt_client.connect("test.mosquitto.org", 1883, 60)
    mqtt_client.loop_start()
    
    mqtt_client.on_connect = callback.on_connect
    mqtt_client.on_publish = callback.on_publish
    
    #TOPIC:
    for type_sensor in TOPIC:
        mqtt_client.subscribe(type_sensor)
    
    mqtt_client.message_callback_add("acm_sensor",callback.acm_sensor_callback)
    mqtt_client.message_callback_add("gyr_sensor",callback.gyr_sensor_callback)
    mqtt_client.message_callback_add("mgt_sensor",callback.mgt_sensor_callback)
    mqtt_client.message_callback_add("gps_sensor",callback.gps_sensor_callback)
    mqtt_client.message_callback_add("als_sensor",callback.als_sensor_callback)


    
def publish(topic, message):
    mqtt_client.publish(topic, message, qos=1)

    
@app.route('/')
def index():
    init_mqtt_client()
    return app.send_static_file('index.html')

@app.route('/acm_sensor', methods=['POST'])
def receive_acm_data():
    # Controlla se la richiesta contiene i dati in formato JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    # Recupera i dati JSON dal corpo della richiesta
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Elabora i dati ricevuti (ad esempio, salvali in un database)
    publish("acm_sensor", json.dumps(data))
    

    return jsonify({'message': 'Data received successfully'}), 200

@app.route('/gyr_sensor', methods=['POST'])
def receive_gyr_data():
    # Controlla se la richiesta contiene i dati in formato JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    # Recupera i dati JSON dal corpo della richiesta
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Estrai i dati dai dati JSON ricevuti

    # Elabora i dati ricevuti (ad esempio, salvali in un database)
    publish("gyr_sensor", json.dumps(data))

    return jsonify({'message': 'Data received successfully'}), 200

@app.route('/mgt_sensor', methods=['POST'])
def receive_mgt_data():
    # Controlla se la richiesta contiene i dati in formato JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    # Recupera i dati JSON dal corpo della richiesta
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Estrai i dati dai dati JSON ricevuti

    # Elabora i dati ricevuti (ad esempio, salvali in un database)
    publish("mgt_sensor", json.dumps(data))

    return jsonify({'message': 'Data received successfully'}), 200

@app.route('/als_sensor', methods=['POST'])
def receive_als_data():
    # Controlla se la richiesta contiene i dati in formato JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    # Recupera i dati JSON dal corpo della richiesta
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Estrai i dati dai dati JSON ricevuti

    # Elabora i dati ricevuti (ad esempio, salvali in un database)
    publish("als_sensor", json.dumps(data))

    return jsonify({'message': 'Data received successfully'}), 200

@app.route('/gps_sensor', methods=['POST'])
def receive_gps_data():
    # Controlla se la richiesta contiene i dati in formato JSON
    if request.headers['Content-Type'] != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    # Recupera i dati JSON dal corpo della richiesta
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format'}), 400

    # Estrai i dati dai dati JSON ricevuti

    # Elabora i dati ricevuti (ad esempio, salvali in un database)
    publish("gps_sensor", json.dumps(data))

    return jsonify({'message': 'Data received successfully'}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    
    

    
