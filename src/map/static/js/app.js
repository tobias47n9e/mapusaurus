var mymap = L.map('mapid').setView([9.822, 47.16377], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'your.mapbox.project.id',
    accessToken: 'your.mapbox.public.access.token'
}).addTo(mymap);

// geometry aus postgis
//console.log(geometry);

var myStyle = {
  "color": '#ff0000',
  "weight": 500,
  "opacity": 1,
};

L.geoJSON(geometry, {
  style: myStyle
}).addTo(mymap);
