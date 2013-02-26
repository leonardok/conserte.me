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



$("#new_problem_message_checkbox").click(function(){
	if ( $("#new_problem_message_checkbox").prop('checked') ){
		$.cookie('problem_message_checkbox', false, { expires: 30 });
	}
});


$('#janela_novo_problema').on('hidden', function () {
	$('#map_canvas').gmap('clear', 'markers');
})

$('#send_new_issue').click(function(){
	// do not process if this is disabled
	if ( $('#send_new_issue').hasClass("disabled") ) { return }

	var bValid = true;
	$("#errors_list").text('');
	if( !$('#name').val() ) {
		$("#errors_list").append('<li>Nome n&atilde;o pode ser vazio.</li>');
		$('.alert.alert-error').show();
		bValid = false;
	}
	if( $('#name').val().length > 100 ) {
		$("#errors_list").append('<li>Nome n&atilde;o pode conter mais de 100 caracteres.</li>');
		$('.alert.alert-error').show();
		bValid = false;
	}

	if( !$('#description').val() ) {
		$("#errors_list").append('<li>Descri&ccedil;&atilde;o n&atilde;o pode ser vazio.</li>');
		$('.alert.alert-error').show();
		bValid = false;
	}
	if( $('#description').val().length > 1000 ) {
		$("#errors_list").append('<li>Descri&ccedil;&atilde;o n&atilde;o pode conter mais de 1000 caracteres.</li>');
		$('.alert.alert-error').show();
		bValid = false;
	}
	if ( !bValid ) {
		$("#dialog-form").spin(false);
		$("#dialog-form").height('auto');
		$("#new-issue-form").show();
		return false;
	}

	$('#send_new_issue').addClass('disabled');
	$('#cancel_new_issue').addClass('disabled');
	
	$('#new_problem_form').hide();
	$('.modal-body').spin();

	data_to_post = '{ "issue": { "name": "'+$('#name').val()+'", "description": "'
		+ $('#description').val()+'", "latitude": "' + $('#latitude').val()
		+ '", "longitude": "' + $('#longitude').val() + '" } }';

	$.ajax ({
		type: "POST",
		//the url where you want to sent the userName and password to
		url: '/api/issues/',
		dataType: 'json',
		async: true,

		data: data_to_post,
		success: function (data) {
			url = "/issues/" + data.issue.id;
			$(location).attr('href',url);
		}
	}).error(function(){
		$("#errors_list").append('<li>Ocorreu um erro. Por favor repita a operação.</li>');
		$('.alert.alert-error').show();

		$('#send_new_issue').removeClass('disabled');
		$('#cancel_new_issue').removeClass('disabled');
		
		$('#new_problem_form').show();
		$('.modal-body').spin(false);
	});
});

$(document).ready(function() {
	init_map();

	if ($.cookie('problem_message_checkbox') == null) {
		$('#how_to_mark').modal('show');
	}
});
