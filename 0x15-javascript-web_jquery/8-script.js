const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url)
.done(function (data) {
	for (let i = 0; i < data.count; i++) {
		const movie = '<i>' + data.results[i].title + '</li>';
		$('#list_movies').append(movie);
	}
});
