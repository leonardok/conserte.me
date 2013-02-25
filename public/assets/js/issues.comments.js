$('#issue_comment_form').submit(function() {
  ret = true;
  $('.alert.alert-error').hide();
  $("#errors_list").text('');

  if( !$('#id_name').val() ) {
    $("#errors_list").append('<li>Nome n&atilde;o pode ser vazio.</li>');
    $('.alert.alert-error').show();
    ret = false;
  }

  if( !$('#id_comment').val() ) {
    $("#errors_list").append('<li>Descri&ccedil;&atilde;o n&atilde;o pode ser vazio.</li>');
    $('.alert.alert-error').show();
    ret = false;
  }
  
  return ret;
});
