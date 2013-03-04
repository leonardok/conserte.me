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


function clean_follow_issue_form(){
	$('#modal-follow-issue').spin(false);
	$('#btn-follow-issue').removeClass('disabled');
	$('#btn-cancel-follow-issue').removeClass('disabled');
	$('#modal-follow-issue').modal('hide');

	$("#form_follow_issue").show();
	$('#follower_email').val('');
	$('#help-follower-invalid-email').hide();
	$('#name_control_group').removeClass('error');
}

function add_error_to_follow_issue_form(){
	$('#name_control_group').addClass('error');
	$('#help-follower-invalid-email').show();
}

function add_follower_success(){
	clean_follow_issue_form();

	$('#page-alert-success .text').text('Seguidor adicionado!');
	$('#page-alert-success').show();
}

function add_follower_error(){
	clean_follow_issue_form();

	$('#page-alert-error').show();
}


function submit_issue_follower(){
	// do not process if this is disabled
	if ( $('#btn-follow-issue').hasClass("disabled") ) { return }

	valid = true;
	var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (re.test($('#follower_email').val()) == false) valid = false;
	if ($('#follower_email').val().length < 1) valid = false;

	if (valid == false){
		add_error_to_follow_issue_form();
		return false;
	}
	
	$('#page-alert-success').hide();
	$('#page-alert-error').hide();
	$("#form_follow_issue").hide();
	$('#modal-follow-issue').spin();

	$('#btn-follow-issue').addClass("disabled");
	$('#btn-cancel-follow-issue').addClass("disabled");

	// $("#form_follow_issue").submit();

	data_to_post = { 
		"email": $('#follower_email').val(),
		"issue_id": $('#issue_id').val(),
	};

	$.ajax ({
		type: 'POST',
		url: '/api/issues/add_follower/',
		contentType: 'application/json; charset=utf-8',
		dataType: 'text',
		async: true,

		data: $.toJSON(data_to_post),
		success: function (data) { add_follower_success(); }
	}).error(function(data){
		response = $.parseJSON(data.responseText);

		if (response.id == 1) { $('#page-alert-error .text').text('Seguidor não pode ser adicionado: já é seguidor!'); }
		else { $('#page-alert-error .text').text('Seguidor não pode ser adicionado: um erro ocorreu!'); }

		add_follower_error();
	});

}


$('#btn-cancel-follow-issue').click(function(){
	// do not process if this is disabled
	if ( $('#btn-follow-issue').hasClass("disabled") ) { return }

	clean_follow_issue_form();
	$('#page-alert-error').hide();
	$('#page-alert-success').hide();
});

$('#btn-follow-issue').click(function(){ submit_issue_follower(); }); 
$('#form_follow_issue').submit(function(){ submit_issue_follower(); return false; });

$(document).ready(function() { init_map(); });
