var map;
var service;
const markers = [];
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

var dummy_resources = {
	"city": {
		"0": "Belgrade",
		"1": "Novi Sad",
		"2": "Nis",
		"3": "Zemun",
		"4": "Kragujevac",
		"5": "Subotica",
		"6": "Valjevo",
		"7": "Loznica",
		"8": "Zrenjanin",
		"9": "Pancevo"
	},
	"resources": {
		"0": 2757.364,
		"1": 760.0,
		"2": 366.328,
		"3": 323.192,
		"4": 301.246,
		"5": 211.362,
		"6": 180.624,
		"7": 172.826,
		"8": 153.022,
		"9": 152.406
	}
}

function initMap() {

    let options = {
        center: { lat: 44.787197, lng: 20.457273 },
        zoom: 7
    }

    map = new google.maps.Map(document.getElementById("map"), options);

    service = new google.maps.places.PlacesService(map);

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

    for (let i = 0; i < 11; i++) {
        console.log(dummy_resources.city[i]);
        markPlaceByNameAddInfoWindow(dummy_resources.city[i], dummy_resources.resources[i]);
    }
    //markPlaceByName(dummy_resources.city[0]);

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


function markPlaceByNameAddInfoWindow(name, available) {
    fetch("https://api.mapbox.com/geocoding/v5/mapbox.places/" + name + ".json?access_token=pk.eyJ1Ijoibm9idWxsaSIsImEiOiJja25kNnByNmcwbGN1MnZvN3ZzZ2h5N3l2In0.yrsXOOfcJ8UxMN-jEyZIqA")
        .then(response => response.json())
        .then(data => {
            console.log(data.features[0]);
            let latLng = new google.maps.LatLng(data.features[0].geometry.coordinates[1], data.features[0].geometry.coordinates[0])
            let marker = new google.maps.Marker({
                position: latLng,
                map: map
            })

            markers.push(marker);

            let infoWindow = new google.maps.InfoWindow({
                content: `<h3><strong>${name}</strong> - Dostupno: ${available}</h3>`
            })

            marker.addListener("click", () => {
                infoWindow.open(map, marker);
            })
        })
}