$(document).ready(function () {
    $(".slider-for").slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        speed: 500,
        arrows: false,
        fade: true,
        asNavFor: ".slider-nav"
    });
    $(".slider-nav").slick({
        slidesToShow: 5,
        slidesToScroll: 1,
        speed: 500,
        arrows: true,
        asNavFor: ".slider-for",
        centerMode: true,
        focusOnSelect: true,
        slide: "div",
    });

});