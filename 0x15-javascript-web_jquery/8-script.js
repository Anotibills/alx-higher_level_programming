/*JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json*/
$.get('https://swapi.co/api/films/?format=json', function(data) {
  $.each(data.results, function(index, result) {
    $('#list_movies').append('<li>' + result.title + '</li>');
  });
});
