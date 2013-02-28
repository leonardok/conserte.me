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

function remove_errors() {
	$("#name_control_group").removeClass('error');
	$("#email_control_group").removeClass('error');
	$("#description_control_group").removeClass('error');

	$("#name_error").hide();
	$("#email_error").hide();
	$("#description_error").hide();
}


$('#janela_novo_problema').on('hidden', function () {
	$('#map_canvas').gmap('clear', 'markers');
	remove_errors();
})

$('#send_new_issue').click(function(){
	// do not process if this is disabled
	if ( $('#send_new_issue').hasClass("disabled") ) { return }

	var bValid = true;
	$("#errors_list").text('');
	if( !$('#name').val() ) {
		$("#name_control_group").addClass('error');
		$("#name_error").text('Título não pode ser vazio');
		$("#name_error").show();
		bValid = false;
	}
	if( $('#name').val().length > 100 ) {
		$("#name_control_group").addClass('error');
		$("#name_error").text('Título não pode ter mais de 100 caracteres');
		$("#name_error").show();
		bValid = false;
	}

	// For now we will let the email to be empty
	// if( !$('#description').val() ) {
	// 	$("#email_control_group").addClass('error');
	// 	$("#email_error").text('Email não pode ser vazio');
	// 	$("#email_error").show();
	// 	bValid = false;
	// }
	if( $('#email').val().length > 100 ) {
		$("#email_control_group").addClass('error');
		$("#email_error").text('Email não pode ter mais de 100 caracteres');
		$("#email_error").show();
		bValid = false;
	}

	if( !$('#description').val() ) {
		$("#description_control_group").addClass('error');
		$("#description_error").text('Descrição não pode ser vazio');
		$("#description_error").show();
		bValid = false;
	}
	if( $('#description').val().length > 1000 ) {
		$("#description_control_group").addClass('error');
		$("#description_error").text('Descrição não pode ter mais de 1000 caracteres');
		$("#description_error").show();
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

	data_to_post = { 
		"issue": {
			"name": $('#name').val(),
			"description": $('#description').val(),
			"latitude": $('#latitude').val(),
			"longitude": $('#longitude').val()
		}
	};

	$.ajax ({
		type: 'POST',
		url: '/api/issues/',
		contentType: 'application/json; charset=utf-8',
		dataType: 'text',
		async: true,

		data: $.toJSON(data_to_post),
		success: function (data) {
			url = "/issues/";
			url += $.parseJSON(data).id;
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
