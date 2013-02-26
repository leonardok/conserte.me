var enable_location_query = true;
var glog_marker = "";



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
			glob_marker = $('#map_canvas').gmap('addMarker', { 
				'position': event.latLng, 
				'draggable': true, 
				'bounds': false }, function(map, marker) {

				// do whatever you need with the maker utilizing this variable
				$('#latitude').val(marker.position.lat());
				$('#longitude').val(marker.position.lng());
				$('#janela_novo_problema').modal('show')
                  });
                });
	});
}


$( "#dialog-form" ).dialog({
   autoOpen: false,
   width: 350,
   modal: true,
   buttons: {
     Cancel: function() {
       $( this ).dialog( "close" );
     },
     "Enviar": function() {
       $("#new-issue-form").hide();
       $("#dialog-form").height('200px');
       $("#dialog-form").spin();

       var bValid = true;
       $("#errors_list").text('');
       if( !$('#name').val() ) {
         $("#errors_list").append('<li>Nome n&atilde;o pode ser vazio.</li>');
         $('.alert.alert-error').show();
         bValid = false;
       }

       if( !$('#description').val() ) {
         $("#errors_list").append('<li>Descri&ccedil;&atilde;o n&atilde;o pode ser vazio.</li>');
         $('.alert.alert-error').show();
         bValid = false;
       }
       if ( !bValid ) {
	 $("#dialog-form").spin(false);
         $("#dialog-form").height('auto');
         $("#new-issue-form").show();
         return false;
       }

       $.ajax ({
             type: "POST",
             //the url where you want to sent the userName and password to
             url: '/api/issues/',
             dataType: 'json',
             async: false,
             
             data: '{ "issue": { "name": "'+$('#name').val()+'", "description": "'+$('#description').val()+'", "latitude": "' + $('#latitude').val() + '", "longitude": "' + $('#longitude').val() + '" } }',
             success: function (data) {
             	url = "/issues/" + data.issue.id;
             	$(location).attr('href',url);

             	$("#dialog-form").dialog( "close" );
             }
         })

     },
   },
   close: function() {
     //allFields.val( "" ).removeClass( "ui-state-error" );
     $('#map_canvas').gmap('clear', 'markers');
   }
 });


$( "#create-user" )
	.button()
	.click(function() {
	$( "#dialog-form" ).dialog( "open" );
});

$('#janela_novo_problema').on('hidden', function () {
	$('#map_canvas').gmap('clear', 'markers');
})

$(document).ready(function() {
	init_map();
});
