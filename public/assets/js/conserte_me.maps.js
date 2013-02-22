function load_markers_for_bounds(){
	$('#map_canvas').gmap('get', 'map').getBounds()

	var a = $('#map_canvas').gmap('get', 'map').getBounds().getSouthWest().lat() + ',' + $('#map_canvas').gmap('get', 'map').getBounds().getSouthWest().lng()
	var b = $('#map_canvas').gmap('get', 'map').getBounds().getNorthEast().lat() + ',' + $('#map_canvas').gmap('get', 'map').getBounds().getNorthEast().lng()

	$.getJSON('api/issues', {
		filter_area: 'true',
		lat_sw: $('#map_canvas').gmap('get', 'map').getBounds().getSouthWest().lat(),
		lng_sw: $('#map_canvas').gmap('get', 'map').getBounds().getSouthWest().lng(),
		lat_ne: $('#map_canvas').gmap('get', 'map').getBounds().getNorthEast().lat(),
		lng_ne: $('#map_canvas').gmap('get', 'map').getBounds().getNorthEast().lng(),
	}, function(data){
		$.each( data, function(i, m) {
			$('#map_canvas').gmap('addMarker', { 'position': new google.maps.LatLng(m.latitude, m.longitude), 'bounds':false} 
			).click(function() {
				//var content = 'TEXT_AND_HTML_IN_INFOWINDOW' + m.id
				var content = "<a href='/issues/" + m.id + "'><h4>#" + m.id + ": " + m.name + "</h4></a>" + "<p>" + m.description + "</p>";
				$('#map_canvas').gmap('openInfoWindow', { 'content': content }, this);
			});
		});

		$('#active-at_location').html(data.length);
		
	});

}
var map = $('#map_canvas').gmap({ 
                        'scrollwheel': false, 
                        'mapTypeControl': false,
                      })
	// executes when ready
	.bind('init', function(ev, map) {
		// first set the zoom
		$('#map_canvas').gmap('option', 'zoom', 14);
		$('#map_canvas').gmap('option', 'center', new google.maps.LatLng(-30.031278, -51.226158));

		// do an initial load for problems
		load_markers_for_bounds($('#map_canvas').gmap('get', 'map').getBounds());

		$(map).dragend(function(event){ 
			load_markers_for_bounds();
		});

		$(map).addEventListener('zoom_changed', function(event){
			load_markers_for_bounds();
		});
	});
