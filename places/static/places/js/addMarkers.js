function addMarkers(markers, map){
	console.log('add markers')
	for(var i = 0; i < markers.length; i++){
		var marker = new google.maps.Marker({
			position:{lat: markers[i][1], lng: markers[i][2]},
			map: map,
			title: markers[i][0]
		});		
	}
}
