$(document).ready(function () {
    jQuery(".slider-child").draggable({
    cursor: "move",
    containment: "parent",
    stop: function() {
      if(jQuery(".slider-child").position().left < 1)
          jQuery(".slider-child").css("left", "720px");
    }
});


    // $('.selector').mousewheel(function(e, delta) {
    //     this.scrollLeft -= (delta * 40);
    //     e.preventDefault();
    // });


  // var APP = APP || {};
  //
  // APP.menu = function () {
  //   $('.sub-menu-trigger').click(function() {
  //     $('.sub-menu').stop().slideToggle();
  //   })
  // };
  //
  // APP.menu();
});
