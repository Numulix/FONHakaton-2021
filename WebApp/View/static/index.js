var map;

function initMap() {

    let options = {
        center: { lat: 44.787197, lng: 20.457273 },
        zoom: 8
    }

    map = new google.maps.Map(document.getElementById("map"), options);
    hourlyEq();
	
	  map.data.setStyle(function(feature) {
		var magnitude = feature.getProperty('mag');
		return {
		  icon: getCircle(magnitude)
		};
	  });
}

function hourlyEq() {
    fetch("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson")
        .then(response => response.json())
        .then(data => {
            features = data.features;

            const heatmapData = [];

            for (let i = 0; i < features.length; i++) {
                let lat = features[i].geometry.coordinates[1];
                let lng = features[i].geometry.coordinates[0];
                let latLng = new google.maps.LatLng(lat, lng);
				let magnitude = features[i].properties.mag;
				
				let txt = " ";
				
				if (i < 10) {
					txt = "Grad:" + city_data[i*2] + "\nPopulacija:" + city_data[i*2+1];
				}
                
                heatmapData.push(latLng);

                new google.maps.Marker({
                    position: latLng,
                    map: map,
					label: { color: '#00aaff', fontWeight: 'bold', fontSize: '14px', text: txt }
                })

                const circle = new google.maps.Circle({
				  strokeColor: "#FF0000",
				  strokeOpacity: 0.8,
				  strokeWeight: 2,
				  fillColor: "#FF0000",
				  fillOpacity: 0.35,
				  map,
				  center: latLng,
				  radius: Math.pow(2, magnitude)/2,
				});
            }

            new google.maps.visualization.HeatmapLayer({
                data: heatmapData,
                dissipating: false,
                map: map
            })

        });
}