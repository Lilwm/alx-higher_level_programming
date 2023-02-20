// select the DIV#red_header element, 
// and adds the class "red" to the <header> element when the user clicks on it
$(document).ready(function() {
    $('#red_header').click(function() {
      $('header').addClass('red');
    });
  });