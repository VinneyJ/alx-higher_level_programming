$(function () {
  const $title = $('#list_movies');
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      $.each(data.results, function (i, film) {
        const item1 = $('<li></li>').text(film.title);
        $title.append(item1);
      });
    }
  });
});
