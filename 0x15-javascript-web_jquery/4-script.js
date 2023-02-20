//toggles the class of the <header> element using jQuery when the user clicks on the tag DIV#toggle_header:
$(document).ready(function(){
    $('#toggle_header').click(function(){
      $('header').toggleClass('red green');
    });
  });
  