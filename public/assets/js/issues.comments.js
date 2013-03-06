$('#issue_comment_form').submit(function() {
	var ret = true;
	var errors_text = '<h4>Erros:</h4><ul>';

	$('.alert.alert-error').hide();
	$(".alert.alert-error.text").text('');

	
	var regex = /^[#$%^&*()]+$/;

	if( !$('#id_name').val() ) {
		errors_text += '<li>Nome n&atilde;o pode ser vazio.</li>' ;
		ret = false;
	} else if (regex.test($('#id_name').val())) {
		errors_text += '<li>Caracteres especiais encontrados no seu coment&aacute;io.</li>';
		ret = false;
	}


	if( !$('#id_comment').val() ) {
		errors_text += '<li>Descri&ccedil;&atilde;o n&atilde;o pode ser vazio.</li>';
		ret = false;
	} else if (regex.test($('#id_comment').val())) {
		errors_text += '<li>Caracteres especiais encontrados no seu coment&aacute;io.</li>';
		ret = false;
	}
	
	if( !ret ){
		errors_text += '</ul>';
		$(".alert.alert-error .text").prop('innerHTML', errors_text);
		$('.alert.alert-error').show();
	}

	return ret;
});
