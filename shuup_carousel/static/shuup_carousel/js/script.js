// Set up owl carousel for product list with 3 items
$(".owl-carousel.four").each(function() {
    var arrowsVisible = JSON.parse($(this).data("arrowsVisible").toLowerCase());
    $(this).owlCarousel({
        margin: 30,
        nav: arrowsVisible,
        navText: [
            '<i class="fa fa-angle-left .carousel-control .icon-prev"></i>',
            '<i class="fa fa-angle-right .carousel-control .icon-prev"></i>'
        ],
        responsiveClass: true,
        responsive: {
            0: { // breakpoint from 0 up
                items : 1,
            },
            640: { // breakpoint from 640 up
                items : 2,
            },
            992: { // breakpoint from 992 up
                items : 4,
            }
        }
    });
});
