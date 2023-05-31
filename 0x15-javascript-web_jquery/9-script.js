const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.get(url + $('html')[0].lang)
.done(function (data) {
	$('#hello').text(data(data.hello);
});
