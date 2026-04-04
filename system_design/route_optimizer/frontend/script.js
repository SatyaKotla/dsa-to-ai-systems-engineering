// 1. Global Variables
let map;
let start = null;
let end = null;
let markers = [];
let authToken = localStorage.getItem("token");

let selectedMap = "grid_10"; // default
let gridLayers = [];
let gridNodeLayer = null;

let routeLine = null;
let glowLine = null;
let movingMarker = null;

const startIcon = new L.Icon({
    iconUrl: './assets/marker_green.svg',
    iconSize: [40, 50],
    iconAnchor: [16, 32]
});

const endIcon = new L.Icon({
    iconUrl: './assets/marker_red.svg',
    iconSize: [40, 50],
    iconAnchor: [16, 32]
});

const carIcon = L.divIcon({
    className: "car-icon",
    html: `<img id="car" src="./assets/car.svg" style="width:32px; transform-origin:center;" />`,
    iconSize: [32, 32],
    iconAnchor: [16, 16]
});

// 2. Initialization
map = L.map("map").setView([40.7580, -73.9855], 13);

const tileLayer =  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

function setNYCView(){
    map.setView([40.7580, -73.9855], 13);
}

// 3. Event Listeners

// 3.1 Drop Down
document.getElementById("mapSelector").addEventListener("change", loadSelectedMap);

// Map Loader function
function loadSelectedMap(){
    selectedMap = document.getElementById("mapSelector").value;

    //console.log("Selected map:", selectedMap);

    // Reset everything when map changes
    resetMap();
    clearGrid();

    const gridSize = getGridSize(selectedMap);

    if (gridSize){

        // Grid Mode
        map.removeLayer(tileLayer);
        drawGrid(gridSize); // Grid lines
        drawGridNodes(gridSize); // Grid Nodes
    } else {
        // OSM Mode
        map.addLayer(tileLayer);
        clearGrid();
        setNYCView();
    }
}

// 4. Core Logic

// 4.1 Handle Map Click
map.on("click", function(e){
    const {lat, lng} = e.latlng;

    const gridSize = getGridSize(selectedMap);

    // Snap ONLY for grid maps
    const [finalLat, finalLng] = gridSize
        ? snapToGrid(lat, lng, gridSize)
        : [lat, lng];

    if (!start){
        start = [finalLat, finalLng];
        addMarker(finalLat, finalLng, "Start", "start");
    } else if (!end){
        end = [finalLat, finalLng];
        addMarker(finalLat, finalLng, "End", "end");

        getRoute(); // call backend
    } else {
        // reset
        showMessage("Route already exists. Press reset to start again.", "warning");
    }
});

// 4.2 Grid Logic



function clearGrid(){
    gridLayers.forEach(layer => map.removeLayer(layer));
    gridLayers = [];

    // Remove node layer (LayerGroup)
    if (gridNodeLayer){
        map.removeLayer(gridNodeLayer);
        gridNodeLayer = null;
    }
}

// draw grid
function drawGrid(size){

    for (let i=0; i < size; i++){

        // vertical lines
        const vLine = L.polyline([[0, i], [size-1, i]], {
            color: "gray",
            weight: 1
        }).addTo(map);

        // Horizontal lines
        const hLine = L.polyline([[i, 0], [i, size-1]], {
            color: "gray",
            weight: 1
        }).addTo(map);

        gridLayers.push(vLine, hLine);
    }

    // Fit map to grid
    map.fitBounds([
        [0, 0],
        [size-1, size-1]
    ]);
}

// Detect Grid Size from Name
function getGridSize(mapName){
    if (mapName.startsWith("grid_")){
        return parseInt(mapName.split("_")[1]);
    }

    return null;
}

// Draw Nodes function
function drawGridNodes(gridSize){

    // Remove old nodes
    if (gridNodeLayer){
        map.removeLayer(gridNodeLayer);
    }

    gridNodeLayer = L.layerGroup().addTo(map);

    for (let x = 0; x < gridSize; x++){
        for (let y = 0; y < gridSize; y++){

            const lat = x;
            const lng = y;

            L.circleMarker([lat, lng], {
                radius: 4,
                color: "#111827",
                fillColor: "111827",
                fillOpacity: 1
            }).addTo(gridNodeLayer);
        }
    }
}

// 4.3 API Call
async function login() {

    if (authToken) return; // prevent repeated login

    try{
        const response = await fetch("https://route-optimizer-gateway.onrender.com/login",{
            method: "POST",
        });

        const data = await response.json();
        authToken = data.access_token;
        localStorage.setItem("token", authToken);

        console.log("Logged in successfully");
    } catch (error){
        console.error("Login failed", error);
    }

}
async function getRoute() {

    const loading = document.getElementById("loading");

    if (!start || !end) return;

    const API_BASE_URL = "https://route-optimizer-gateway.onrender.com";

    loading.style.visibility = "visible";

    //login
    if (!authToken){
        await login();
    }

    let response = await fetch(`${API_BASE_URL}/route`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + authToken,
        },
        body: JSON.stringify({
            map: selectedMap,
            start_lat: start[0],
            start_lon: start[1],
            end_lat: end[0],
            end_lon: end[1],
            include_coordinates: true

        })
    });

    // handle expiry
    if (response.status == 401) {
        console.log("Token expired, logging in again...");

        localStorage.removeItem("token");
        authToken=null;

        await login();

        //retry once
        response = await fetch(`${API_BASE_URL}/route`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer " + authToken,
            },
            body: JSON.stringify({
                map: selectedMap,
                start_lat: start[0],
                start_lon: start[1],
                end_lat: end[0],
                end_lon: end[1],
                include_coordinates: true

            })
        });
    }

    const data = await response.json();

    //console.log("API response:", data);

    if (!data.coordinates){

        loading.style.visibility = "hidden";

        console.error("No coordinates in response!");
        showMessage("Coordinates too far from map", "error")
        return;
    }

    animateRoute(data.coordinates);

    loading.style.visibility = "hidden";

    showMessage("Route calculated successfully", "info")

    document.getElementById("distance").innerText =
        `Distance: ${data.distance.toFixed(2)} meters`;
}

// 4.4 Animation
function animateRoute(coordinates){

    // Remove old lines first
    if (routeLine) {
        map.removeLayer(routeLine);
    }

    if (glowLine){
        map.removeLayer(glowLine);
    }

    if (movingMarker){
        map.removeLayer(movingMarker);
    }

    let index = 0;

    routeLine = L.polyline([], {
        color: "#7c3aed",
        weight: 6,
        opacity: 0.9
    }).addTo(map);

    // Glow layer
    glowLine = L.polyline([], {
        color: "#93c5fd",
        weight: 10,
        opacity: 0.4
    }).addTo(map);

    // Create moving marker at the start
    movingMarker = L.marker(coordinates[0], {icon: carIcon}).addTo(map);

    function drawStep(){
        if (index >= coordinates.length) return;

        routeLine.addLatLng(coordinates[index]);
        glowLine.addLatLng(coordinates[index]);

        // Move marker
        movingMarker.setLatLng(coordinates[index]);

        // Rotation
        if (index > 0){
            const prev = coordinates[index - 1];
            const angle = getRotationAngle(prev, coordinates[index]);

            const markerElement = document.getElementById("car");
            if (markerElement){
                markerElement.style.transform = `rotate(${angle}deg)`;
            }
        }

        index++;

        setTimeout(drawStep, 200); // speed control
    }

    drawStep();

}

// 4.5 Reset Map
function clearMap(){
    markers.forEach(m => map.removeLayer(m));
    markers = [];

    if (routeLine){
        map.removeLayer(routeLine);
        routeLine = null;
    }

    // Reset distance
    document.getElementById("distance").innerText = "Distance: --";
}

function resetMap(){
    clearMap();
    start = null;
    end = null;

    // Reset distance
    document.getElementById("distance").innerText = "Distance: --";

    // Reset animation
    if (routeLine) {
        map.removeLayer(routeLine);
        routeLine= null;
    }

    if (glowLine) {
        map.removeLayer(glowLine);
        glowLine = null;
    }

    if (movingMarker) {
        map.removeLayer(movingMarker);
        movingMarker = null;
    }
    // Reset message
    document.getElementById("message").style.display = "none";
}

// 5. UI Helpers

// 5.1 Add markers
function addMarker(lat, lon, label, type){

    let icon = null;

    if (type==="start"){
        icon = startIcon;
    } else if (type==="end"){
        icon = endIcon;
    }

    const marker = L.marker([lat, lon], {icon: icon}).addTo(map)
        .bindPopup(label)
        .openPopup();
    markers.push(marker);
}

// 5.2 Message
function showMessage(text, type="info"){

    const _message = document.getElementById("message");

    _message.innerText = text;

    // Reset classes
    _message.className = "";
    _message.classList.add(`message-${type}`);

    _message.style.display = "block";

    // Auto hide after 3 seconds
    setTimeout(() => {
        _message.style.display = "none";
    }, 3000);
}

// 5.3 Grid Snapping (snaps grid to nearest node)
function snapToGrid(lat, lon, size){
    return [
        Math.round(lat),
        Math.round(lon)
    ];
}

// 5.4 Rotation Function
function getRotationAngle(p1, p2){
    const latDiff = p2[0] - p1[0];
    const lngDiff = p2[1] - p1[1];

    const angle = Math.atan2(lngDiff, latDiff) * (180 / Math.PI);

    return angle;
}

// 6. APP Entry Point
function initializeMap(){
    const gridSize = getGridSize(selectedMap);

    if (gridSize){
        map.removeLayer(tileLayer);
        drawGrid(gridSize);
    } else {
        map.addLayer(tileLayer);
    }
}

// call once on load
initializeMap();
loadSelectedMap();
