// Center zoom and defaultBounds are constant so it must be checket that fit all markers
var map
function initLocationsMap() {
	console.log("init map");
	var center = {lat: 19.30, lng: -99.65};
	if (readCookie("center")) center = JSON.parse(readCookie("center"));
	var zoom = 12;
	if (readCookie("zoom")) zoom = parseInt(readCookie("zoom"));
	mapOptions = {
		center: center,
		zoom: zoom,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		mapTypeControl: false,
		streetViewControl: false,
	};
	map = new google.maps.Map(document.getElementById('map'), mapOptions);

	var input = document.getElementById('pac-input');
	map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

	addListener();

	//code for autocomplete
	var defaultBounds = new google.maps.LatLngBounds(
		new google.maps.LatLng(19.110743, -99.874965),
		new google.maps.LatLng(19.482734, -99.462291)
	);
	autocompleteOptions = {
		bounds: defaultBounds,
		types: ['geocode']
	};
	var autocomplete = new google.maps.places.Autocomplete(input, autocompleteOptions);

	autocomplete.addListener('place_changed', function() {
		console.log("input chaged");
		var place = autocomplete.getPlace();
		var bounds = new google.maps.LatLngBounds();
		bounds.union(place.geometry.viewport);
		map.fitBounds(bounds);
	});
}


function addListener(){
	map.addListener('idle', function(){
		console.log("load results");
		var bounds = new google.maps.LatLngBounds();
		var bounds = map.getBounds();
		$('#results').load("results/?bounds="+JSON.stringify(bounds.toJSON()));
		document.cookie = "center="+JSON.stringify(map.getCenter());
		document.cookie = "zoom="+map.getZoom();
	});
}