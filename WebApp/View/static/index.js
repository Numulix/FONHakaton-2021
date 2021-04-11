var map;
const circles = [];

var dummy_epicenters = [
    {
        epicenter: [44.117512, 20.189369],
        magnitude: 6
    }, {
        epicenter: [43.886935, 20.556935],
        magnitude: 7
    }, {
        epicenter: [43.654546, 20.838094],
        magnitude: 7
    }]

function initMap() {

    let options = {
        center: { lat: 44.787197, lng: 20.457273 },
        zoom: 7
    }

    map = new google.maps.Map(document.getElementById("map"), options);

    for (let i = 0; i < dummy_epicenters.length; i++) {
        let latLng = new google.maps.LatLng(dummy_epicenters[i].epicenter[0], dummy_epicenters[i].epicenter[1])
        circles.push(new google.maps.Circle({
            strokeColor: "#FF0000",
			strokeOpacity: 0.8,
			strokeWeight: 2,
			fillColor: "#FF0000",
			fillOpacity: 0.35,
			map,
            center: latLng,
            radius: Math.pow(2, dummy_epicenters[i].magnitude) * 100
        }))
    }

    hourlyEq();
	
	  map.data.setStyle(function(feature) {
		var magnitude = feature.getProperty('mag');
		return {
		  icon: getCircle(magnitude)
		};
	  });
}

function hourlyEq() {
    fetch("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson")
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

function addMarker() {
    let lat = document.getElementById("latitude").value
    let lng = document.getElementById("longitude").value

    let latLng = new google.maps.LatLng(lat, lng)
    new google.maps.Marker({
        position: latLng,
        map: map
    })
}