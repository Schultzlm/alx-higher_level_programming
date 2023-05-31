$('#toggle_header'.click(function () {
	if ($('header').hasClass('green')) {
		$('header').addClass('red');
		$('header').removeClass('green');
	} else {
		$('header').addClass('green');
		$('header').removeClass('red');
	}
});
