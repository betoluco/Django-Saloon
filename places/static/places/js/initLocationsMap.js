// Center zoom and defaultBounds are constant so it must be checket that fit all markers
function initLocationsMap() {
	console.log("init map");
	var zoom = 12;
	if(readCookie("zoom")) zoom = +readCookie("zoom");
	var latlng = {lat: 19.3031489, lng: -99.6275017};
	if(readCookie("center")) latlng = JSON.parse(readCookie("center"));
	mapOptions = {
		center: latlng,
		zoom: zoom,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		mapTypeControl: false,
		streetViewControl: false,
	};
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);
	var input = document.getElementById('pac-input');
	map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

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
	getMarkers(map);
	addListener(map);
}