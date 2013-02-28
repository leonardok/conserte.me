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


$('#cancel-photo').click(function(){
	// do not process if this is disabled
	if ( $('#cancel-photo').hasClass("disabled") ) { return }

	$("#photo-upload-form").show();
	$('#modal-upload-photo').spin(false);
});

$('#btn-send-photo').click(function(){
	// do not process if this is disabled
	if ( $('#btn-send-photo').hasClass("disabled") ) { return }
	
	$('#btn-send-photo').addClass("disabled");
	$("#photo-upload-form").hide();
	$('#modal-upload-photo').spin();
	$("#photo-upload-form").submit();
});

$(document).ready(function() {
	init_map();
});
