// Set up owl carousel http://www.owlcarousel.owlgraphic.com/docs/api-options.html
$(".owl-carousel.one").each(function() {
    var autoplay = JSON.parse($(this).data("autoplay"));
    var interval = JSON.parse($(this).data("interval"));
    var arrowsVisible = JSON.parse($(this).data("arrows-visible").toLowerCase());
    var pauseOnHover = JSON.parse($(this).data("pause-on-hover").toLowerCase());
    var useDotNavigation = JSON.parse($(this).data("use-dot-navigation").toLowerCase());
    $(this).owlCarousel({
        loop: true,
        autoplay: autoplay,
        autoplayTimeout: interval,
        autoplayHoverPause: pauseOnHover,
        nav: arrowsVisible,
        navText: [
            '<i class="fa fa-angle-left .carousel-control .icon-prev"></i>',
            '<i class="fa fa-angle-right .carousel-control .icon-prev"></i>'
        ],
        dots: useDotNavigation,
        items: 1
    });
});
