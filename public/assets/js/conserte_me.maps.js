var enable_location_query = true;


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
				var content = "<a href='/issues/" + m.id + "'><h4>#" + m.id + ": " + m.name + "</h4></a>" + "<p>" + m.description + "</p>";
				$('#map_canvas').gmap('openInfoWindow', { 'content': content }, this);
			});
		});
		current_address();

		$('#active-at_location').html(data.length);
		
	});

}

function current_address(){
	if (enable_location_query == false) return;

	var center = $('#map_canvas').gmap('get', 'map').getCenter();
	var geocoder = new google.maps.Geocoder();
	var latlng = new google.maps.LatLng(center.lat(), center.lng());


	// Set a cookie for the last center
	$.cookie("lat", center.lat(), { expires : 10, domain: "conserte.me" });
	$.cookie("lng", center.lng(), { expires : 10, domain: "conserte.me" });


	geocoder.geocode({'latLng': latlng}, function(results, status) {
		if (status == google.maps.GeocoderStatus.OK) {
			if (results[1]) {
				var city = "";
				var state = "";
				var i = 0;
				for (i=0;i < results[1].address_components.length;i++){
					if ($.inArray('locality', results[1].address_components[i].types) != -1){
						city = results[1].address_components[i].long_name;
					}
					else if ($.inArray('administrative_area_level_1', results[1].address_components[i].types) != -1){
						state = results[1].address_components[i].short_name;
					}
					else if ($.inArray('country', results[1].address_components[i].types) != -1){
						country= results[1].address_components[i].short_name;
					}
				}
				text = "Voce esta em: "
				if (city != "") text = text + city + ', ';
				if (state != null) text = text + state;
				$('#current_location').text(text);

				var link = "issues/" + country + '/' + state + '/' + city.replace(/ /g,'') + '/?page=1';
				$('#current_location_probs_a').attr('href', link); 
			}
		} else { }

		enable_location_query = false;
		setTimeout(function(){
			enable_location_query = true;
		},1000);
	});
}

var map = $('#map_canvas').gmap({ 
                        //'scrollwheel': false, 
                        'mapTypeControl': false,
                      })
	// executes when ready
	.bind('init', function(ev, map) {
		// first set the zoom
		$('#map_canvas').gmap('option', 'zoom', 14);

		if($.cookie('lat') == null || isNaN($.cookie('lat'))) { 
			latlng = new google.maps.LatLng(-30.031278, -51.226158);
		} else {
			lat= $.cookie('lat');
			lng= $.cookie('lng');
			latlng = new google.maps.LatLng(lat, lng);
		}
		$('#map_canvas').gmap('option', 'center', latlng);

		// do an initial load for problems
		load_markers_for_bounds($('#map_canvas').gmap('get', 'map').getBounds());

		$(map).dragend(function(event){ 
			load_markers_for_bounds();
		});

		$(map).addEventListener('zoom_changed', function(event){
			load_markers_for_bounds();
		});

		current_address();
	});

