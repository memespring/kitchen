$( document ).ready(function() {
  setInterval("getData()",3000);
});

function getData() { 
  $.getJSON("/data", function(result){
    $('#message').html('');
    for (i = 0; i < result['message'].length; i++) {
      $('#message').append('<span>' + result['message'][i] + '</span>')
    }
    $('#message').bigtext(); 
  });
}
