
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

// // Hemophilia gallery
// const activity_image = document.querySelectorAll(".activity_gallery_slide");
// var counter = 0;
// activity_image.forEach(
//   (slide, index) => {
//     slide.style.left = `${index * 100}%`
//   }
// )