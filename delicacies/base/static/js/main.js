(function ($) {
    "use strict";


// Facts counter
    $('[data-toggle="counter-up"]').counterUp({
        delay: 10,
        time: 2000
    });

// Initiate the wowjs
    new WOW().init();


// Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });    

    window.addEventListener('DOMContentLoaded', () => {
        lucide.createIcons();   
    });

})(jQuery);

