$(document).ready(function () {

const slider = $(".slider-child");
slider
  .slick({
  dots: true,
  infinite: true,
  speed: 300,
  variableWidth: true,

          responsive: [
        {
            breakpoint: 767,
             settings: {
                    centerMode:true,
                    arrows:false,
                    autoplay: true,
                    autoplaySpeed: 4000,
                }
        }
    ]
  });


slider.on('wheel', (function(e) {
  e.preventDefault();


  if (e.originalEvent.deltaY < 0) {
    $(this).slick('slickNext');
  } else {
    $(this).slick('slickPrev');
  }
}));


});

