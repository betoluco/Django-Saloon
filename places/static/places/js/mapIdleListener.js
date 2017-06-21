function addListener(map){
	map.addListener('idle', function(){
		console.log("load results");
		var bounds = new google.maps.LatLngBounds();
		var bounds = map.getBounds();
		$('#results').load("results/?bounds="+JSON.stringify(bounds.toJSON()));
	});
}