//select the DIV#red_header element, 
//and updates the text color of the <header> element to red when the user clicks on it
$(document).ready(function() {
    $('#red_header').click(function() {
      $('header').css('color', '#FF0000');
    });
  });