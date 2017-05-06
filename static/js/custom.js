$(document).ready(function(){
    $(".close-menu").click(function(){
        $(".mobile-menu").animate({left: "-=100vw"}, 300);
    });
    $("#menu-mobile-icon").click(function(){
        $(".mobile-menu").animate({left: "+=100vw"}, 300);
    });

})
