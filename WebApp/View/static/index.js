var map;

function initMap() {

    let options = {
        center: { lat: 44.787197, lng: 20.457273 },
        zoom: 8
    }

    map = new google.maps.Map(document.getElementById("map"), options);
}