    // Crear mapa
const map = L.map('map').setView([36.21415, -5.38663], 19);  
console.log("Mapa iniciado")
// Tiles OpenStreetMap
L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxNativeZoom: 24,
    maxZoom: 24,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
}).addTo(map);

let circles = [];

async function cargarPuntos() {

    try {

        // Eliminar círculos anteriores
        circles.forEach(circle => {
            map.removeLayer(circle);
        });

        circles = [];

        // Consultar API Django
        const response = await fetch('/points/?t=' + Date.now(), {
            cache: "no-store"
        });
        const data = await response.json();

        // Añadir nuevos puntos
        data.forEach(point => {

            const circle = L.circle([point.lat, point.lon], {
                radius: 1,
                color: '#ffffff',
                weight: 1,
                fill: true,
                fillColor: '#d9ff00',
                fillOpacity: 1,
            })
            .addTo(map)
            .bindPopup(`Speed: ${point.speed} km/h`);

            // Guardar referencia
            circles.push(circle);

        });

        console.log("Puntos actualizados:", data.length);

    } catch (error) {

        console.error("Error cargando puntos:", error);

    }
}

// Primera carga
cargarPuntos();

// Actualizar cada 5 segundos
setInterval(cargarPuntos, 5000);