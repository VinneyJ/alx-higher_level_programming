$('document').ready(function () {
  const hello = $("#hello");
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: function (data){
      hello.text(data.hello);
    }
  });
  
});
