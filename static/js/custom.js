
//https://owlcarousel2.github.io/OwlCarousel2/docs/started-welcome.html
$(document).ready(function(){
  $('#header-carousel').owlCarousel({
    items : 1,
    loop : true,
    autoplay:true,
    dots:false,
    autoplayTimeout:4000,
  });
})


// $(document).ready(function(){
//   $('#hemo-news').owlCarousel({
//     rtl:false,
//     loop:true,
//     margin:10,
//     nav:true,
//     autoplay:true,
//     autoplayTimeout:5000,
//     responsive:{
//         0:{
//             items:2
//         },
//         600:{
//             items:2
//         },
//         1000:{
//             items:4
//         }
//     }
// })
// })

// $(document).ready(function(){
//   $('#presosan').owlCarousel({
//     rtl:false,
//     loop:true,
//     margin:10,
//     nav:true,
//     autoplay:true,
//     autoplayTimeout:5000,
//     responsive:{
//         0:{
//             items:2
//         },
//         600:{
//             items:2
//         },
//         1000:{
//             items:4
//         }
//     }
// })
// })

$('.hemophilia-gallery').owlCarousel({
    items : 1,
    loop : true,
    autoplay:true,
    dots:true,
    nav:true,
    autoplayTimeout:4000,
})


// Detail page translator
let btn_english = document.getElementById('btn_english')
if(btn_english != null){
  btn_english.onclick = function(){
    english();
  }
}

let btn_hindi = document.getElementById('btn_hindi')
if(btn_hindi != null){
  btn_hindi.onclick = function(){
    hindi();
}
}

function english(){
    document.getElementById('hindi').style.display = 'none';
    document.getElementById('english').style.display = 'block';
    document.getElementById('default_content').innerHTML = '';
}
function hindi(){
    document.getElementById('hindi').style.display = 'block';
    document.getElementById('english').style.display = 'none';
    document.getElementById('default_content').innerHTML = '';
}