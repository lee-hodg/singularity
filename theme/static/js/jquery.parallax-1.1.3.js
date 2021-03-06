/*
Plugin: jQuery Parallax
Version 1.1.3
Author: Ian Lunn
Twitter: @IanLunn
Author URL: http://www.ianlunn.co.uk/
Plugin URL: http://www.ianlunn.co.uk/plugins/jquery-parallax/

Dual licensed under the MIT and GPL licenses:
http://www.opensource.org/licenses/mit-license.php
http://www.gnu.org/licenses/gpl.html
*/

(function( $ ){
	var $window = $(window);
	var windowHeight = $window.height();
	var windowWidth = $window.width();
    //console.log('Px: windowHeight:', windowHeight);
    //console.log('Px: windowWidth:', windowWidth);

	$window.resize(function () {
		windowHeight = $window.height();
		windowWidth = $window.width();
	});

	$.fn.parallax = function(xpos, speedFactor, outerHeight) {
		var $this = $(this);
		var getHeight;
		var firstTop;
		var paddingTop = 0;
		
		//get the starting position of each element to have parallax applied to it		
		$this.each(function(){
		    firstTop = $this.offset().top;

            //DEBUG
            //console.log('this id:', $this.attr('id'));
            //console.log('Px:firstTop:', firstTop);
            //console.log("Px: $('#section-parallax').offset().top", $('#section-parallax').offset().top);
            //console.log("$('#section-parallax').height()", $('#section-parallax').height());
            //console.log("$('#section-slideshow').height()", $('#section-slideshow').height());
		});

		if (outerHeight) {
			getHeight = function(jqo) {
				return jqo.outerHeight(true);
			};
		} else {
			getHeight = function(jqo) {
				return jqo.height();
			};
		}
			
		// setup defaults if arguments aren't specified
		if (arguments.length < 1 || xpos === null) xpos = "50%";
		if (arguments.length < 2 || speedFactor === null) speedFactor = 0.1;
		if (arguments.length < 3 || outerHeight === null) outerHeight = true;
		
		// function to be called whenever the window is scrolled or resized
		function update(){
			var pos = $window.scrollTop();				

			$this.each(function(){
				var $element = $(this);
				var top = $element.offset().top;
				var height = getHeight($element);

				// Check if totally above or totally below viewport
                // I added the windowWidth to disable on tablets and mobiles too.
				if (top + height < pos || top > pos + windowHeight || windowWidth < 768) {
					return;
				}

                //DEBUG
                //console.log('window.width() is:', windowWidth);
                //console.log('window.scrollTop scrollbar pos:', pos);
                //console.log('element top is:', top);
                //console.log('element height is:', height);
                //console.log('elment firstTop is:', firstTop);
                //console.log('set bg ypos to: Math.round((firstTop - pos) * speedFactor):', Math.round((firstTop - pos) * speedFactor));
                //console.log('************************');

				$this.css('backgroundPosition', xpos + " " + Math.round((firstTop - pos) * speedFactor) + "px");
			});
		}		

		$window.bind('scroll', update).resize(update);
		update();
	};
})(jQuery);
