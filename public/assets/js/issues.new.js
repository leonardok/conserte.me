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
			});
		});
		current_address();

		$('#active-at_location').html(data.length);
		
	});

}


function init_map(){
	var map = $('#map_canvas').gmap({ 'mapTypeControl': false, })
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

		$(map).click( function(event) {
			$('#map_canvas').gmap('addMarker', { 
				'position': event.latLng, 
				'draggable': true, 
				'bounds': false }, function(map, marker) {

				// do whatever you need with the maker utilizing this variable
				$( "#dialog-form" ).dialog( "open" );
                  });
                });
	});
}


$( "#dialog-form" ).dialog({
   autoOpen: false,
   height: 300,
   width: 350,
   modal: true,
   buttons: {
     "Create an account": function() {
       var bValid = true;
       allFields.removeClass( "ui-state-error" );

       bValid = bValid && checkLength( name, "username", 3, 16 );
       bValid = bValid && checkLength( email, "email", 6, 80 );
       bValid = bValid && checkLength( password, "password", 5, 16 );

       bValid = bValid && checkRegexp( name, /^[a-z]([0-9a-z_])+$/i, "Username may consist of a-z, 0-9, underscores, begin with a letter." );
       // From jquery.validate.js (by joern), contributed by Scott Gonzalez: http://projects.scottsplayground.com/email_address_validation/
       bValid = bValid && checkRegexp( email, /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i, "eg. ui@jquery.com" );
       bValid = bValid && checkRegexp( password, /^([0-9a-zA-Z])+$/, "Password field only allow : a-z 0-9" );

       if ( bValid ) {
         $( "#users tbody" ).append( "<tr>" +
           "<td>" + name.val() + "</td>" +
           "<td>" + email.val() + "</td>" +
           "<td>" + password.val() + "</td>" +
         "</tr>" );
         $( this ).dialog( "close" );
       }
     },
     Cancel: function() {
       $( this ).dialog( "close" );
     }
   },
   close: function() {
     //allFields.val( "" ).removeClass( "ui-state-error" );
   }
 });


$( "#create-user" )
	.button()
	.click(function() {
	$( "#dialog-form" ).dialog( "open" );
});

$(document).ready(function() {
	init_map();
	
});
