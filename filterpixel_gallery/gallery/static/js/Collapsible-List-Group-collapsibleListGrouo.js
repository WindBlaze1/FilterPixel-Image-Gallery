$("button").click(function(){
  $("button").removeClass("active");
  $(this).addClass("active");
});

$(function() {
        
  $('.list-group-item').on('click', function() {
    $('.fas', this)
      .toggleClass('fa-angle-right')
      .toggleClass('fa-angle-down');
  });

});