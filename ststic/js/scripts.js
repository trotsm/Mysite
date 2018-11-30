$(document).ready(function() {

  var APP = APP || {};

  APP.menu = function () {
    $('.sub-menu-trigger').click(function() {
      $('.sub-menu').stop().slideToggle();
    })
  };

  APP.menu();

});
