let deviceCounters = {};
let maps = {}
let markers = {}

// Funzione per aggiornare i valori dei sensori e incrementare i contatori
function updateSensor(deviceId, sensor, values) {
    let device = document.getElementById(deviceId);
    if (!device) return;

    if (sensor === 'acm') {
        device.querySelector('.acm_x').innerText = values.x.toFixed(2);
        device.querySelector('.acm_y').innerText = values.y.toFixed(2);
        device.querySelector('.acm_z').innerText = values.z.toFixed(2);
        deviceCounters[deviceId].acm++;
        device.querySelector('.acm_counter').innerText = deviceCounters[deviceId].acm;
    } else if (sensor === 'gyr') {
        device.querySelector('.gyr_x').innerText = values.x.toFixed(2);
        device.querySelector('.gyr_y').innerText = values.y.toFixed(2);
        device.querySelector('.gyr_z').innerText = values.z.toFixed(2);
        deviceCounters[deviceId].gyr++;
        device.querySelector('.gyr_counter').innerText = deviceCounters[deviceId].gyr;
    } else if (sensor === 'mgt') {
        device.querySelector('.mgt_x').innerText = values.x.toFixed(2);
        device.querySelector('.mgt_y').innerText = values.y.toFixed(2);
        device.querySelector('.mgt_z').innerText = values.z.toFixed(2);
        deviceCounters[deviceId].mgt++;
        device.querySelector('.mgt_counter').innerText = deviceCounters[deviceId].mgt;
    } else if (sensor === 'gps') {
        // Aggiornamento della posizione sulla mappa
        updateMap(deviceId, values.latitude, values.longitude);
        deviceCounters[deviceId].gps++;
        device.querySelector('.gps_counter').innerText = deviceCounters[deviceId].gps;
    } else if (sensor === 'als') {
        device.querySelector('.als_value').innerText = values.illuminance.toFixed(2);
        deviceCounters[deviceId].als++;
        device.querySelector('.als_counter').innerText = deviceCounters[deviceId].als;
    }
}

// Funzione per aggiornare il nome del dispositivo
function updateDeviceName(deviceId, name) {
    let device = document.getElementById(deviceId);
    if (!device) return;

    device.querySelector('.device-name-value').innerText = name;
}


function updateMap(deviceId, lat, lon) {
    let device = document.getElementById(deviceId);
    const mapContainer = device.querySelector('.map-container');

    if (!maps[deviceId]) {
        const map = L.map(mapContainer).setView([lat, lon], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19
        }).addTo(map);
        const marker = L.marker([lat, lon]).addTo(map);

        maps[deviceId] = map
        markers[deviceId] = marker
    } else {
        maps[deviceId].setView([lat, lon],13);
        markers[deviceId].setLatLng([lat, lon]); 
    }
    
}


// Funzione per aggiungere un nuovo dispositivo
function addDevice(deviceId, deviceName) {
    const initialMessage = document.getElementById('initial-message');
    if (initialMessage) {
        initialMessage.style.display = 'none';
    }

    let template = document.querySelector('.template');
    let deviceTemplate = template.cloneNode(true);
    deviceTemplate.classList.remove('template');
    deviceTemplate.id = deviceId;
    deviceTemplate.style.display = 'block';
    deviceTemplate.querySelector('.device-name-value').innerText = deviceName;

    // Inizializza contatori per il nuovo dispositivo
    deviceCounters[deviceId] = {
        acm: 0,
        gyr: 0,
        mgt: 0,
        gps: 0,
        als: 0
    };

    document.getElementById('devices-container').appendChild(deviceTemplate);
}

