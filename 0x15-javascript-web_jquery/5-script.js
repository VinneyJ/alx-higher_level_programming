$('DIV#add_item').click(function () {
  const item = $('<li></li>').text('Item2');
  $('UL.my_list').prepend(item);
});
