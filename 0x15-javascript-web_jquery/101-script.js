$(document).ready(function () {
  $('div').click(function () {
    $('.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('.my_list > :last-child, .my_list > :first-child').remove();
  });
  $('#clear_list').click(function () {
    $('.my_list').empty();
  });
});
