const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url)
.done(function(data) {
	$('#character').replaceWith(data.name);
});
