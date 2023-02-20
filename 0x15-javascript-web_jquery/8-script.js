//fetches and lists all movie titles:
$(document).ready(function() {
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
      var movieTitles = data.results.map(function(movie) {
        return '<li>' + movie.title + '</li>';
      });
      $('#list_movies').html(movieTitles.join(''));
    });
  });
  