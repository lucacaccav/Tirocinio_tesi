let devices = [];
let deviceNumber = 1; 

function addDeviceIfNotExists(deviceName) {
    if (!devices.some(device => device.deviceName === deviceName)) {
        let deviceId = 'device' + deviceNumber; // Generazione dell'ID del dispositivo
        addDevice(deviceId, deviceName); // Aggiunta del dispositivo
        devices.push({ deviceId, deviceName }); // Aggiunta della coppia deviceId e deviceName all'array devices
        deviceNumber++; // Incremento del contatore dei dispositivi
    }
}

function getDeviceId(deviceName) {
    for (let i = 0; i < devices.length; i++) {
        if (devices[i].deviceName === deviceName) {
            return devices[i].deviceId;
        }
    }
    return null; // Restituisci null se non trovi il deviceName
}

function log(message) {
    const logMessagesElement = document.getElementById('log-messages');
    logMessagesElement.textContent += message + '\n';
    logMessagesElement.scrollTop = logMessagesElement.scrollHeight;
}

var socket = io();
socket.on('connect', function() {
    log("Connesso a localhost:5000")
});

socket.on('acm_sensor', (data) => {
    addDeviceIfNotExists(data.userId)
    updateSensor(getDeviceId(data.userId), 'acm', { x: data.x, y: data.y, z: data.z });
    log('Received ACM sensor data: ' + data.userId);
});

socket.on('gyr_sensor', (data) => {
    addDeviceIfNotExists(data.userId)
    updateSensor(getDeviceId(data.userId), 'gyr', { x: data.x, y: data.y, z: data.z });
    log('Received GYR sensor data: ' + data.userId);
});

socket.on('mgt_sensor', (data) => {
    addDeviceIfNotExists(data.userId)
    updateSensor(getDeviceId(data.userId), 'mgt', { x: data.x, y: data.y, z: data.z });
    log('Received MGT sensor data: ' + data.userId);
});

socket.on('gps_sensor', (data) => {
    addDeviceIfNotExists(data.userId)
    updateSensor(getDeviceId(data.userId), 'gps', { latitude: data.latitude, longitude: data.longitude });
    log('Received GPS sensor data: ' + data.userId);
});

socket.on('als_sensor', (data) => {
    addDeviceIfNotExists(data.userId)
    updateSensor(getDeviceId(data.userId), 'als', { illuminance: data.illuminance });
    log('Received ALS sensor data: ' + data.userId);
});