//fetches and display the translated "hello" value:
$(document).ready(function() {
    $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
      $('#hello').text(data.hello);
    });
  });
  