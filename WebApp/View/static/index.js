var map;

function initMap() {

    let options = {
        center: { lat: 44.787197, lng: 20.457273 },
        zoom: 8
    }

    map = new google.maps.Map(document.getElementById("map"), options);
    hourlyEq();
}

function hourlyEq() {
    fetch("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
        .then(response => response.json())
        .then(data => {
            features = data.features;

            for (let i = 0; i < features.length; i++) {
                let lat = features[i].geometry.coordinates[1];
                let lng = features[i].geometry.coordinates[0];
                let latLng = new google.maps.LatLng(lat, lng);

                new google.maps.Marker({
                    position: latLng,
                    map: map
                });
            }

        });
}