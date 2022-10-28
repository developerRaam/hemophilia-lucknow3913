
//https://owlcarousel2.github.io/OwlCarousel2/docs/started-welcome.html
$(document).ready(function(){
  $('#header-carousel').owlCarousel({
    items : 1,
    loop : true,
    autoplay:true,
    autoplayTimeout:4000,
  });
})


$(document).ready(function(){
  $("#hemo-news").owlCarousel({
    items : 3,
    margin:10,
    loop : true,
    nav:false,
    autoplay:true,
    autoplayTimeout:5000,
  });
})
