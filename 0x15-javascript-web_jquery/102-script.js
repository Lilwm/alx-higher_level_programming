//fetches and print the translation of "Hello" based on the language code entered by the user:
$(document).ready(function() {
    $('#btn_translate').click(function() {
      var languageCode = $('#language_code').val();
      var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
      
      $.getJSON(apiUrl, { lang: languageCode }, function(data) {
        $('#hello').text(data.hello);
      });
    });
  });
  