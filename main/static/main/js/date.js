// highlight current day on opeining hours
$(document).ready(function() {
$('.opening-hours li').eq(new Date().getDay()).addClass('today');
});

$(window).scroll(function() {
    if($(this).scrollTop() > 300) {
        $('.navbar-fixed-top').addClass('opaque');
    } else {
        $('.navbar-fixed-top').removeClass('opaque');
    }
});