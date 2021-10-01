$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const item = $('<li></li>').text('Item');
    $('.my_list').append(item);
  });

  $('DIV#remove_item').click(function () {
    $('.my_list li').last().remove();
  });

  $('DIV#clear_list').click(function () {
    $('.my_list').empty();
  });
});
