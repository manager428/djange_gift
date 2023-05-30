(function($) {
    "use strict";

    /* ..............................................
       Loader 
       ................................................. */
    $(window).on('load', function() {
        $('.preloader').fadeOut();
        $('#preloader').delay(550).fadeOut('slow');
        $('body').delay(450).css({
            'overflow': 'visible'
        });
    });

    /* ..............................................
       Fixed Menu
       ................................................. */

    $(window).on('scroll', function() {
        if ($(window).scrollTop() > 50) {
            $('.main-header').addClass('fixed-menu');
        } else {
            $('.main-header').removeClass('fixed-menu');
        }
    });

    /* ..............................................
       Gallery
       ................................................. */

    $('#slides-shop').superslides({
        inherit_width_from: '.cover-slides',
        inherit_height_from: '.cover-slides',
        play: 5000,
        animation: 'fade',
    });

    $(".cover-slides ul li").append("<div class='overlay-background'></div>");

    /* ..............................................
       Map Full
       ................................................. */

    $(document).ready(function() {
        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 100) {
                $('#back-to-top').fadeIn();
            } else {
                $('#back-to-top').fadeOut();
            }
        });
        $('#back-to-top').click(function() {
            $("html, body").animate({
                scrollTop: 0
            }, 600);
            return false;
        });
    });

    /* ..............................................
       Tooltip
       ................................................. */

    $(document).ready(function() {
        $('[data-toggle="tooltip"]').tooltip();
    });

    /* ..............................................
       Scroll
       ................................................. */

    $(document).ready(function() {
        $(window).on('scroll', function() {
            if ($(this).scrollTop() > 100) {
                $('#back-to-top').fadeIn();
            } else {
                $('#back-to-top').fadeOut();
            }
        });
        $('#back-to-top').click(function() {
            $("html, body").animate({
                scrollTop: 0
            }, 600);
            return false;
        });
    });

	/* ..............................................
	   NiceScroll
	   ................................................. */

       $(".brand-box").niceScroll({
		cursorcolor: "#9b9b9c",
	});
	
}(jQuery));