;(function ($) {
    'use strict';

    	
    $.fn.avkonste_init_carousel = function () {

        if( typeof $.fn.slick == 'undefined'){
            console.error('avkonste-Framework need to use slick library inside, pls make sure It was loaded before used');
            return;
        }

        $(this).not('.slick-initialized').each(function () {
            let slide           = $(this),
                default_config  = slide.attr('data-slick'),
                config          = default_config !== undefined ? JSON.parse(default_config) : { arrows: true, dots: false, slidesMargin: 0, slidesToShow: 1, infinite: true, speed: 400};

            if (config.vertical === true ) {
                config.prevArrow = '<span  class="fa-solid fa-chevron-left prev"></span>';
                config.nextArrow = '<span class="fa-solid fa-chevron-right next"></span>';
            } else {
                config.prevArrow = '<span class="fa-solid fa-chevron-right prev"></span>';
                config.nextArrow = '<span class="fa-solid fa-chevron-left next"></span>';
            }

            slide.on('init', function (event, slick) {
                $(event.target).trigger( 'avkonste_trigger_init_slide', slick);
            });
            slide.slick(config);
        });
    };


    $.fn.avkonste_tab = function () {
        $(this).each(function(index,element){
            let TAB = $(this);
            TAB.on('click','.tab-link', function (e) {
                e.preventDefault();
                let $this       = $(this),
                    $tab_head   = $this.closest('li'),
                    tab_id      = $this.attr('href');
                if( !$tab_head.hasClass('active') && typeof tab_id !== undefined){
                    let $active_tab = TAB.find(tab_id);
                    if( $active_tab.length ){
                        $active_tab.siblings('.active').removeClass('active');
                        $active_tab.addClass('active').avkonste_equal_height();
                        $tab_head.siblings('.active').removeClass('active');
                        $tab_head.addClass('active');
                    }
                }
            });
        });
    };
    
}( jQuery ));
;(function($){
    'use strict';
    let $document                                   = $(document),
        $avkonste_slide                              = $('.avkonste-carousel'),
        $block_tab                                  = $('.avkonste-tab-contain')
        
    /*Carousel Handle*/
    if( $avkonste_slide.length){
        $avkonste_slide.avkonste_init_carousel();
    }

    /*Tab button*/
    if( $block_tab.length){
        $block_tab.avkonste_tab();
    }

})(jQuery);


