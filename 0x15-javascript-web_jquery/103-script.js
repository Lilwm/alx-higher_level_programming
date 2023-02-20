//fetch and print the translation of "Hello" based on the language code entered by the user when they 
//click on the #btn_translate button or press ENTER when the focus is on the #language_code
$(document).ready(function() {
    function translateHello() {
      var languageCode = $('#language_code').val();
      var apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
      
      $.getJSON(apiUrl, { lang: languageCode }, function(data) {
        $('#hello').text(data.hello);
      });
    }
    
    $('#btn_translate').click(function() {
      translateHello();
    });
    
    $('#language_code').on('keydown', function(event) {
      if (event.key === 'Enter') {
        translateHello();
      }
    });
  });
  