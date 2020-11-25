mapboxgl.accessToken = 'pk.eyJ1IjoiYXJyYnV6aWsiLCJhIjoiY2tiYnd2ZnFtMDR5bDJwcnFiYjVpZTZ1aCJ9.OuA40zTySKXydSOEX90Oew';

// add map
const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [37.620795, 55.754024],
  zoom: 13
});


// Add a geocoder
// add input search places on map
map.addControl(
  new MapboxGeocoder({
    accessToken: mapboxgl.accessToken,
    mapboxgl: mapboxgl
  })
);


// locate the user
map.addControl(
  new mapboxgl.GeolocateControl({
    positionOptions: {
      enableHighAccuracy: true
    },
    trackUserLocation: true
  })
);

// will contain a list used to filter against
const layerIDs = []; 
const filterInput = document.getElementById('filter-input');


//the first - create fixture database file (include name places and coordinates) 
//the second - create GeoJSON file
fetch("/static/fmapbox.geojson")
.then(response => response.json())
.then(data => {
  const geojson = data // include places, coordinates and other information from fixture file

  map.on('load', function () {
    map.loadImage(
      "/static/materialize/icons/beer.png",

      function (error, image) {
        if (error) throw error;
        map.addImage('custom-marker', image);

        map.addSource('places', {
          'type': 'geojson',
          'data': data
        });

        data.features.forEach(function(feature) {
          let title = feature.properties['title'];
          const layerID = title.toLowerCase();

          // Add a layer showing the places.
          if (!map.getLayer(layerID)) {
            map.addLayer({
              'id': layerID,
              'type': 'symbol',
              'source': 'places',
              'layout': {
                'text-field': title,
                'text-font': [
                'Open Sans Bold',
                'Arial Unicode MS Bold'
                ],
                'text-size': 12,
                'text-transform': 'uppercase',
                'text-letter-spacing': 0.05,
                'text-offset': [0, 1.5],
                'icon-image': 'custom-marker',
                'icon-allow-overlap': true
              },
              'paint': {
                'text-color': '#602',
                'text-halo-color': '#fff',
                'text-halo-width': 2
              },

              'filter': ['==', 'title', title]
            }); 
          }; 
          layerIDs.push(layerID);             
        });

        // Create a popup, but don't add it to the map yet.
        const popup = new mapboxgl.Popup({
          closeButton: false,
          closeOnClick: false
        });

        layerIDs.forEach(function(layer) {
          map.on('mouseenter', layer, function (e) {
            // Change the cursor style as a UI indicator.
            map.getCanvas().style.cursor = 'pointer';

            let coordinates = e.features[0].geometry.coordinates.slice();
            let description = e.features[0].properties.description;

            while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
              coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
            }

            // Populate the popup and set its coordinates
            // based on the feature found.
            popup.setLngLat(coordinates).setHTML(description).addTo(map);
          });

          map.on('mouseleave', layer, function () {
            map.getCanvas().style.cursor = '';
            popup.remove();
          });
        });


        // add input search by filter
        filterInput.addEventListener('keyup', function(e) {
          // If the input value matches a layerID set
          // it's visibility to 'visible' or else hide it.
          let value = e.target.value.trim().toLowerCase();
          layerIDs.forEach(function(layerID) {
            map.setLayoutProperty(
              layerID,
              'visibility',
              layerID.indexOf(value) > -1 ? 'visible' : 'none'
            );
          });
        });
      }
    );
  });
});