var starttxtslide = false, startprofileslide = false;
if ((navigator.userAgent.match(/iPhone/i)) || (navigator.userAgent.match(/iPod/i)) || (navigator.userAgent.match(/iPad/i)) || (navigator.userAgent.match(/Android/i)) || (navigator.userAgent.match(/webOS/i))) {
	eventbtn = "touchstart";
	eventbtn2 = "touchstart";
} else {
	eventbtn = "click";
	eventbtn2 = "hover";
}

$(document).ready(function() {

				
			$('.passwordbox').click(function(){
				$(this).hide();
				$(this).prev().focus();
			});
				

				var d = document;
				var safari = (navigator.userAgent.toLowerCase().indexOf('safari') != -1) ? true : false;
				var gebtn = function(parEl,child) { return parEl.getElementsByTagName(child); };
				onload = function() {
					
					var body = gebtn(d,'body')[0];
					body.className = body.className && body.className != '' ? body.className + ' has-js' : 'has-js';
					
					if (!d.getElementById || !d.createTextNode) return;
					var ls = gebtn(d,'label');
					for (var i = 0; i < ls.length; i++) {
						var l = ls[i];
						if (l.className.indexOf('label_') == -1) continue;
						var inp = gebtn(l,'input')[0];
						if (l.className == 'label_check') {
							l.className = (safari && inp.checked == true || inp.checked) ? 'label_check c_on' : 'label_check c_off';
							l.onclick = check_it;
						};
						if (l.className == 'label_radio') {
							l.className = (safari && inp.checked == true || inp.checked) ? 'label_radio r_on' : 'label_radio r_off';
							l.onclick = turn_radio;
						};
					};
				};
				var check_it = function() {
					var inp = gebtn(this,'input')[0];
					if (this.className == 'label_check c_off' || (!safari && inp.checked)) {
						this.className = 'label_check c_on';
						if (safari) inp.click();
					} else {
						this.className = 'label_check c_off';
						if (safari) inp.click();
					};
				};
				var turn_radio = function() {
					var inp = gebtn(this,'input')[0];
					if (this.className == 'label_radio r_off' || inp.checked) {
						var ls = gebtn(this.parentNode,'label');
						for (var i = 0; i < ls.length; i++) {
							var l = ls[i];
							if (l.className.indexOf('label_radio') == -1)  continue;
							l.className = 'label_radio r_off';
						};
						this.className = 'label_radio r_on';
						if (safari) inp.click();
					} else {
						this.className = 'label_radio r_off';
						if (safari) inp.click();
					};
				};



						$('.sbToggle ').click(function(){
							//$('ul.sbOptions li:first').hide();
							alert('hi');
						});




	if ($('.carouse_thumbs').html() != null) {

		var gethash = (window.location.hash);
		var ulah = new Array();
		var tLiah = new Array();
		var tlah = new Array();
		var liSize = new Array();
		var ulSize = new Array();
		
		$('.btn_prev').css({opacity:0.2});

		for ( i = 0; i < $(".carouse_thumbs").size(); i++) {
			// home bottom gallery sliding
			ulah[i] = $(".carouse_thumbs:eq(" + i + ") .thumbchartgrps");
			tLiah[i] = $(".thumbchart", ulah[i]);
			tlah[i] = tLiah[i].size();
			liSize[i] = (tLiah[i]).width();
			$(".carouse_thumbs:eq(" + i + ") .thumbchartgrps .thumbchart:last").css('margin','0 0px 17px 0');
			// Full li size(incl margin)-Used for animation
			
			if (tlah[i] < 4){
				$(".carouse_thumbs:eq(" + i + ")").prev().css({opacity:0.2});
			}

			ligrpby3 = Math.round(tlah[i]/3)
			widththrice = (parseInt(liSize[i]) + 10) * 3;

			ulSize[i] = (widththrice) * ligrpby3;
			// size of full ul(total length, not just for the visible items)
			tLiah[i].css({
				width : (parseInt(liSize[i])) + "px"
			});
			ulah[i].css("width", ulSize[i] - 10 + "px").css("left", "0");

			//var slideri = ulah[i].parents(".partner_slider:eq("+i+") span.next").find('ul.questslider').index(ulah[i]);
			if (tlah[i] < 3) {
				$(".carouse_thumbs:eq(" + i + ")").prev().addClass('disable');
				$(".carouse_thumbs:eq(" + i + ")").prev().prev().addClass('disable');
			} else {

				$(".carouse_thumbs:eq(" + i + ")").prev().unbind('mousedown');
				$(".carouse_thumbs:eq(" + i + ")").prev().mousedown(function() {
					startfrm=0

					if ($(this).hasClass('disable') == false) {
						var maxleft = 705 - ($(this).next().find('.thumbchartgrps').width());
						// alert(maxleft)
						var offleft = parseInt($(this).next().find('.thumbchartgrps').css('left'), 10);
						duration = (-maxleft + offleft) * 8;
						startfrm = offleft;
						/*$(this).next().find('.thumbchartgrps').stop(false, false).animate({
							'left' : maxleft + 'px'
						}, duration, 'linear');
						*/
						//$(this).parent().find(".partner_slider:eq("+i+") span.prev").show();
					}
				});

				$(".carouse_thumbs:eq(" + i + ")").prev().unbind('mouseup');
				$(".carouse_thumbs:eq(" + i + ")").prev().mouseup(function() {
					if ($(this).hasClass('disable') == false) {
						$(this).next().find('.thumbchartgrps').stop(false, false);

						var maxleft = -($(this).next().find('.thumbchartgrps').width() - 705);
						getleft = $(this).next().find('.thumbchartgrps').stop(false, false).css('left');
						getleft = getleft.replace("px", "");
						startto = getleft;

						//if( getleft <= (maxleft) )
						// $(this).hide();
					}

				});


				$(".carouse_thumbs:eq(" + i + ")").prev().unbind('click');
				$(".carouse_thumbs:eq(" + i + ")").prev().click(function(){

					windoww = $('.carouse_box').width();

					 if ((startfrm-startto)<15){
						  var maxleft = windoww - ($(this).next().find('.thumbchartgrps').width() );
						  var getleft = $(this).next().find('.thumbchartgrps').stop(false,false).css('left')
						  var newoffshet = parseInt(getleft);
						  reducedby = newoffshet;
						  reducedby = reducedby%240;
						  newoffshet = newoffshet - 240 - reducedby;
						  newoffshet = newoffshet - 240;
						  newoffshet = newoffshet - 240;
							
							
							if ($(this).parent().find('.thumbchart').size() < 4){
								$(this).prev().css({opacity:0.2});
							}else{
							  $(this).prev().css({opacity:1});
							}

						  if (newoffshet<=(maxleft+10)){
							  $(this).css({opacity:0.2});
							 newoffshet=maxleft+5;
						  }
							 $(this).next().find('.thumbchartgrps').stop(false,false).animate({'left':newoffshet+'px'},750,'easeOutCubic');

					 }
				 });


				$(".carouse_thumbs:eq(" + i + ")").prev().prev().unbind('mousedown');
				$(".carouse_thumbs:eq(" + i + ")").prev().prev().mousedown(function() {
					if ($(this).hasClass('disable') == false) {
						startfrm=0
						var maxleft = $(this).next().next().find('.thumbchartgrps').width() - 705;
						var offleft = parseInt($(this).next().next().find('.thumbchartgrps').css('left'), 10);
						var duration = -offleft * 8;
						startfrm = offleft;

						/*$(this).next().next().find('.thumbchartgrps').stop(false, false).animate({
							'left' : '0px'
						}, duration, 'linear');
						*/
						//$(this).parent().find(".partner_slider:eq("+i+") span.next").show();
					}
				});

				$(".carouse_thumbs:eq(" + i + ")").prev().prev().unbind('mouseup');
				$(".carouse_thumbs:eq(" + i + ")").prev().prev().mouseup(function() {
					if ($(this).hasClass('disable') == false) {
						$(this).next().next().find('.thumbchartgrps').stop(false, false);
						var getleft = $(this).next().next().find('.thumbchartgrps').css('left');
						getleft = getleft.replace("px", "");

						startto = getleft;

						//if(getleft>=0)
						//$(this).hide();

					}
				});



				$(".carouse_thumbs:eq(" + i + ")").prev().prev().unbind('click');
				 $(".carouse_thumbs:eq(" + i + ")").prev().prev().click(function(){

					 if ((startto-startfrm)<15){

						  var getleft = $(this).next().next().find('.thumbchartgrps').stop(false,false).css('left')
						  var newoffshet = parseInt(getleft);
						  reducedby = newoffshet;
						  newoffshet = newoffshet  ;
						  reducedby = reducedby%240;

							newoffshet = (newoffshet) - reducedby;
							newoffshet = (newoffshet) + 240;
							newoffshet = (newoffshet) + 240;
							newoffshet = (newoffshet) + 240;
							
							
							if ($(this).parent().find('.thumbchart').size() < 4){
								$(this).next().css({opacity:0.2});
							}else{
								$(this).next().css({opacity:1});
							}

						  if (newoffshet > -30){
							  $(this).css({opacity:0.2});
							  newoffshet=0;
						  }
							$(this).next().next().find('.thumbchartgrps').stop(false,false).animate({'left':newoffshet+'px'},750,'easeOutCubic');

					 }
				 });

			}
		}



	}


	$('.skillsWrapper h4').click(function(){
		if ( $(this).hasClass('active')==false)
		{
			$('.skillsWrapper h4').removeClass('active');
			$('.skillsWrapper .skillsContainer').slideUp();
			$('.academicBackground h4').removeClass('active');
			$('.academicBackground .academicBackgroundUl').slideUp();
			$(this).addClass('active');
			$(this).next().slideDown();
		}
	})
	$('.academicBackground h4').click(function(){
		if ( $(this).hasClass('active')==false)
		{
			$('.skillsWrapper h4').removeClass('active');
			$('.skillsWrapper .skillsContainer').slideUp();
			$('.academicBackground h4').addClass('active');
			$('.academicBackground .academicBackgroundUl').slideDown();
		}
	})


// END DOC
});



function nextsliding(newindex){
	
			getw = $('.slidingtxt').width();
				$('.bulletquote li').removeClass('active');
				$('.bulletquote li').eq(newindex).addClass('active');
				if (newindex==0){
					$('.slidingtxt').stop().animate({'width':'569px'},1500,'easeInOutQuad')
					$('.headslide_txt').stop().animate({'width':'600px'},1500,'easeInOutQuad')
					getw=569;
				}else{
					$('.slidingtxt').stop().animate({'width':'619px'},1500,'easeInOutQuad')
					$('.headslide_txt').stop().animate({'width':'650px'},1500,'easeInOutQuad')
					getw=619;
					}
				$('.slidingtxt section').eq(newindex).css({'left':getw+'px','display':'block'})
				$('.slidingtxt section.active').stop().animate({'left':-getw+'px'},1500,'easeInOutQuad',function(){
					$(this).removeClass('active')
				})
				$('.slidingtxt section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
					$(this).addClass('active')
					clearInterval(starttxtslide);
					starttxtslide = 0;
					starttxtslide = setInterval(autonextslide, 8000);
				})
}

function prevsliding(newindex){
			
			getw = $('.slidingtxt').width();
				if (newindex==0){
					$('.slidingtxt').stop().animate({'width':'569px'},1500,'easeInOutQuad')
					$('.headslide_txt').stop().animate({'width':'600px'},1500,'easeInOutQuad')
					getw=569;
				}else{
					$('.slidingtxt').stop().animate({'width':'619px'},1500,'easeInOutQuad')
					$('.headslide_txt').stop().animate({'width':'650px'},1500,'easeInOutQuad')
					getw=619;
					}
			$('.bulletquote li').removeClass('active');
			$('.bulletquote li').eq(newindex).addClass('active');
			$('.slidingtxt section').eq(newindex).css({'left':-getw+'px','display':'block'})
			$('.slidingtxt section.active').stop().animate({'left':'619px'},1500,'easeInOutQuad',function(){
				$(this).removeClass('active');
			})
			$('.slidingtxt section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
				$(this).addClass('active');
					clearInterval(starttxtslide);
					starttxtslide = 0;
				starttxtslide = setInterval(autonextslide, 8000);
			})
}


function autonextslide(){
					clearInterval(starttxtslide);
					starttxtslide = 0;
				getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
				newindex = getindex+1;
				if ($('.slidingtxt section.active').next().html()!=null){
					//newindex=0;
					nextsliding(newindex);
				}
}



function nextprofilslid(elem,newindex){
	getw = elem.find('.slidingprofile').width();
	elem.find('.slidingprofile section').eq(newindex).css({'left':getw+'px','display':'block'})
	elem.find('.slidingprofile section.active').stop().animate({'left':-getw+'px'},1500,'easeInOutQuad',function(){
		$(this).removeClass('active')
	})
	clearInterval(startprofileslide);
	startprofileslide = 0;
	elem.find('.slidingprofile section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
		$(this).addClass('active')
		startprofileslide = setInterval(autonextslide_prof, 10000);
	})
}

function prevprofilslid( elem ,newindex){
	getw = elem.find('.slidingprofile').width();
	elem.find('.slidingprofile section').eq(newindex).css({'left':-getw+'px','display':'block'})
	elem.find('.slidingprofile section.active').stop().animate({'left':getw+'px'},1500,'easeInOutQuad',function(){
		$(this).removeClass('active')
	})
	clearInterval(startprofileslide);
	startprofileslide = 0;
	elem.find('.slidingprofile section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
		$(this).addClass('active')
		startprofileslide = setInterval(autonextslide_prof, 10000);
	})
}
function autonextslide_prof(){
					clearInterval(startprofileslide);
					startprofileslide = 0;
				getindex = $('.headslide_profile.active .slidingprofile section').index( $('.headslide_profile.active .slidingprofile section.active') );
				newindex = getindex+1;
				if ($('.headslide_profile.active .slidingprofile section.active').next().html()==null){
					newindex=0;
				}
				elem = $('.headslide_profile.active');
					nextprofilslid(elem,newindex);
}

window.onresize = function(event) {
	reloadtop();
}

function reloadtop(){
		geth = $(window).height();
		getheader =  $('header').outerHeight(true);
		geth = geth - getheader;


		if ( $('.heading_txt').html()!=null){
			getsection = $('.heading_txt').height();
			getsection2 = $('.quote_container').height();
			geth = geth-getsection-getsection2-30;
			if (geth<0)
				geth=0;
			geth =geth/2;
			$('.heading_txt').css({'margin-top':geth+'px'});
		}

		if ( $('.slidingtxt section').html()!=null){
			getsection = $('.headslide_txt').height();
			geth = geth-getsection-50;
			if (geth<0)
				geth=0;
			geth =geth/2;
			$('.headslide_txt').css({'margin-top':geth+'px'});

		}
		if ( $('.slidingprofile section').html()!=null){
			getsection = $('ul.tabs li:first').outerHeight(true);
			getsection2 = $('.headslide_profile:visible').height();
			geth = geth-getsection-getsection2;
			if (geth<0)
				geth=0;
			geth =geth/2;
			$('ul.tabs').css({'margin-top':geth+'px'});
		}

		if ( $('.callmegrp').html()!=null){
			getsection = $('.callmegrp .leftbracket').height();
			getsection=140;
			geth = geth-getsection-50;
			if (geth<0)
				geth=0;
			geth =geth/2;
			$('.callmegrp').css({'margin-top':geth+'px'});

		}

}



function focuspwd(getval, jqelem){
	//if ( $(jqelem).val() == ''){
		$(jqelem).next().hide();
	//}
}

function blurpwd(getval, jqelem){
	if ( $(jqelem).val() == ''){
		$(jqelem).next().show();
	}
}

