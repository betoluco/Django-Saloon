function initLocationsMap() {
	console.log("function initLocationsMap()");
	mapOptions = {
	center: {lat: 19.3031489, lng: -99.6275017},
    	zoom: 12,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		mapTypeControl: false,
		streetViewControl: false,
	};
	var map = new google.maps.Map(document.getElementById('map'), mapOptions);
	var input = document.getElementById('pac-input');
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
    getMarkers(map);
    addListener(map);
}