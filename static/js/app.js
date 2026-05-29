    // Crear mapa
const map = L.map('map').setView([36.21415, -5.38663], 19);  
console.log("esto es una prueba")
// Tiles OpenStreetMap
L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxNativeZoom: 24,
    maxZoom: 24,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

// Cargar puntos desde Django
fetch('/points/')
    .then(response => response.json())
    .then(data => {
        data.forEach(point => {
            L.circle([point.lat, point.lon], {
                radius: 1,
                color:'#ffffff',
                weight: 1,
                fill: true,
                fillColor: '#d9ff00',
                fillOpacity: 1,
            }).addTo(map).bindPopup(`Speed: ${point.speed} km/h`);
            /*
            L.marker([point.lat, point.lon])
                .addTo(map)
                .bindPopup(`
                    Speed: ${point.speed} km/h
                `);*/

        });

    });