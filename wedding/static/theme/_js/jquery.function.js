//gmap address
var gMapNewAdress = "Kordon Caddesi, Marmaris, Turkiye"

// tweeter
jQuery(function($)
	{
        $(".tweet").tweet({
          join_text: "auto",
          username: "geceolurken",
          count: 2,
          auto_join_text_default: "", //we said,
          auto_join_text_ed: "", //we
          auto_join_text_ing: "", //we were
          auto_join_text_reply: "", //we replied
          auto_join_text_url: "", //we were checking out
          loading_text: "loading tweets..."
        });
	});
	
// slides
$(function(){
	$('#slides').slides({
		preload: true,
		preloadImage: '_images/loading.gif',
		play: 50000,
		pause: 25000,
		hoverPause: true,
		effect: 'slide'
	});
});

// scroller
$(document).ready(function(){
	$(".scroller").click(function(event){
		
		event.preventDefault();

	
		var full_url = this.href;

		
		var parts = full_url.split("#");
		var trgt = parts[1];

		var target_offset = $("#"+trgt).offset();
		var target_top = target_offset.top;


		$('html, body').animate({scrollTop:target_top}, 900);
	});
});		

// gift registry
jQuery(document).ready(function() {
    jQuery('#gift3').jcarousel({
    	wrap: 'circular',
		scroll: 3
    });
});

jQuery(document).ready(function() {
    jQuery('#gift2').jcarousel({
    	wrap: 'circular',
		scroll: 2
    });
});

jQuery(document).ready(function() {
    jQuery('#gift1').jcarousel({
    	wrap: 'circular',
		scroll: 1
    });
});


// rsvp-form
$(document).ready(function()
	{
		$("#rsvpForm").submit(function(){
		var str = $(this).serialize();

		$.ajax({
		type: "POST",
		url: "_php/rsvp.php",
		data: str,
		success: function(msg){
			
		$("#note").ajaxComplete(function(event, request, settings){
			if(msg == 'OK')
			{
			result = '<p style="color:green;">Message sent. Thank you!.</p>';
			}
			else
			{
			result = msg;
			}

			$(this).html(result).fadeIn("slow");
			$(this).html(result);

		});

		}

		 });
		return false;
		});
	});
	
// contact-form
$(document).ready(function()
	{
		$("#contactForm").submit(function(){
		var str = $(this).serialize();

		$.ajax({
		type: "POST",
		url: "_php/contact.php",
		data: str,
		success: function(msg){
			
		$("#note").ajaxComplete(function(event, request, settings){
			if(msg == 'OK')
			{
			result = '<p style="color:green;">Message sent. Thank you!.</p>';
			}
			else
			{
			result = msg;
			}

			$(this).html(result).fadeIn("slow");
			$(this).html(result);

		});

		}

		 });
		return false;
		});
	});
	
//pretty-image
$(document).ready(function(){
	$(".content a[rel^='prettyPhoto']").prettyPhoto({animationSpeed:'slow',theme:'dark_square',slideshow:2000, autoplay_slideshow: false});
});

//pretty-video
$(document).ready(function(){
	$(".three-column-double a[rel^='prettyVideo']").prettyPhoto({animationSpeed:'slow',theme:'dark_square',slideshow:2000, autoplay_slideshow: false});
});

//gmap
$(document).ready(function(){
	$("#map").gMap({ address: gMapNewAdress, zoom:15 });
});

