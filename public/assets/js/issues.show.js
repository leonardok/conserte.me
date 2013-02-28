function init_map(){
	var map = $('#map_canvas_small').gmap({ 'mapTypeControl': false, 'zoomControl': false,
			'panControl': false, 'streetViewControl': false, 'draggable': false})
	// executes when ready
	.bind('init', function(ev, map) {
		// first set the zoom
		$('#map_canvas_small').gmap('option', 'zoom', 14);

		latlng = new google.maps.LatLng( $('#latitude').text(), $('#longitude').text() );
		$('#map_canvas_small').gmap('option', 'center', latlng);

		glob_marker = $('#map_canvas_small').gmap('addMarker', { 
			'position': latlng,
			'draggable': false,
			'bounds': false });
	});
}


$('#btn-send-photo').click(function(){
	$("#photo-upload-form").submit();
});

$(document).ready(function() {
	init_map();
});
