var starttxtslide = false, startprofileslide = false,down_x,up_x, autoplay=true;
if ("ontouchstart" in document.documentElement)
{
	eventbtn = "touchstart";
	eventbtn2 = "touchstart";
} else {
	eventbtn = "click";
	eventbtn2 = "hover";
}




$(document).ready(function() {

			if ( $('section#home').html()!=null){

				if ($('.welcomename').html()==null){
					//$('.overlay').fadeIn();
					//$('.invitebox').fadeIn();
				}

				var offseth = $('#home').offset();
				if ( $(window).height() > 540 ){
					var winh = $(window).height() 
					//$('section#home').css({'background-size':'auto '+winh+'px'});
					//$('#home').css('background-position', '0 ' + (-(0-offseth.top-35)*0.3)+'px');
				}else{
					//$('section#home').css({'background-size':'100% auto'});
					//$('#home').css('background-position', '50% ' + (-(0-offseth.top-35)*0.3)+'px');
				}
			}

			if ( $('.centerl_container').html()!=null){
				var winh = $(window).height()-150;
				$('.centerl_container').css({'min-height': winh +"px"});
				$('.challengebox').css({'min-height': winh +"px"});
				$('.boxgrey3').css({'min-height': winh-40 +"px"});
				if ($('.ppbox').html()!=null) {
					$('.ppbox').css({'min-height': winh+16 +"px"});
				}
			}else if( $('.full_container').html()!=null){
				var winh = $(window).height()-140;
				$('.full_container').css({'min-height': winh +"px"});
				if ($('.wrapper_col1').html()!=null)
					$('.wrapper_col1').css({'min-height': winh +"px"});
			}

			if ( $('.verification_col2').html()!=null){
				var winh = $(window).height()-190;
				$('.verification_col2').css({'min-height': winh +"px"});
				$('.verificationlist').css({'min-height': winh+13 +"px"});

				if ( ($('.verificationlist').height()+30) > $('.verification_col2').height() ){
					if ( $('#QuestionForm').html()!=null )
						var geth = $('.verificationlist').height()-5;
					else
						var geth = $('.verificationlist').height()+0;
					$('.verification_col2').height(geth);
				}else{
					var geth = $('.verification_col2').height();
					$('.verificationlist').height(geth);
				}
			}

			if ( $('.slidingtxt').html()!=null){
				var winh = $(window).height()-150;
				$('section').css({'min-height': winh +"px"});
				$('.slidingtxt').css({'height': winh +"px"});
			}else if ( $('section').html()!=null){
				var h50per = window.innerHeight/2;
				var winh = window.innerHeight + h50per;
				$('section').css({'min-height': winh +"px"});
				//$('section#home').css({'min-height': $(window).height() +"px"});
				$('section:first').css({'min-height': window.innerHeight +"px"});
				var seclen = $('section').size();
				for(i=0;i<seclen;i++){
					geth = $('section').eq(i).find('div').height();
					topmiddle = ($('section').eq(i).height()-h50per)/2 - geth/2 - 30
					$('section > div').eq(i).css({'top': topmiddle +"px"});
				}
				
				geth = $('section').eq(0).find('div').height();
				$('section:first > div').css({'top': (($('section').eq(0).height())/2 - geth/2) - 75 +"px"});
				//$('section:first div').css({'top': (($('section').eq(0).height())/2 - geth/2) +"px"});
			}
			if ( $('.verificationlist').html()!=null  ){
				$('body').addClass('bgwhite');
			}

			if ( $('.thumbchartgrps').html()!=null){
				if ( $('.challengebox .thumbchartgrps').html()==null)
					$('body').addClass('bgwhite2');
			}

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

						/*if (l.className == 'label_check') {
							l.className = (safari && inp.checked == true || inp.checked) ? 'label_check c_on' : 'label_check c_off';
							l.onclick = check_it;
						};*/
						if (l.className == 'label_radio') {
							l.className = (safari && inp.checked == true || inp.checked) ? 'label_radio r_on' : 'label_radio r_off';
							l.onclick = turn_radio;
						};
					};
				};
				/*
				var check_it = function() {
					var inp = gebtn(this,'input')[0];
					if (this.className == 'label_check c_off' || (!safari && inp.checked)) {
						this.className = 'label_check c_on';
						if (safari) inp.click();
					} else {
						this.className = 'label_check c_off';
						if (safari) inp.click();
					};
				};*/
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

			ligrpby3 = Math.ceil(tlah[i]/3)
			widththrice = (parseInt(liSize[i]) + 10) * 3;

			ulSize[i] = (widththrice) * ligrpby3;
			// size of full ul(total length, not just for the visible items)
			tLiah[i].css({
				width : (parseInt(liSize[i])) + "px"
			});
			ulah[i].css("width", ulSize[i] + 10 + "px").css("left", "0");

			//var slideri = ulah[i].parents(".partner_slider:eq("+i+") span.next").find('ul.questslider').index(ulah[i]);
			if (tlah[i] < 3) {
				$(".carouse_thumbs:eq(" + i + ")").prev().addClass('disable');
				$(".carouse_thumbs:eq(" + i + ")").prev().prev().addClass('disable');
			} else {

				$(".carouse_thumbs:eq(" + i + ")").prev().unbind('mousedown');
				$(".carouse_thumbs:eq(" + i + ")").prev().mousedown(function() {
					startfrm=0

					if ($(this).hasClass('disable') == false) {
						var maxleft = 725 - ($(this).next().find('.thumbchartgrps').width());
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

						var maxleft = -($(this).next().find('.thumbchartgrps').width() - 725);
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
						var maxleft = $(this).next().next().find('.thumbchartgrps').width() - 725;
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
$('.overlay, .pop_close, .closepop').click(function(){
	$('.overlay').fadeOut()
	$('.popup').fadeOut()
	$('.tabcontentpop').fadeOut()

	});

	$('.accesslinkmenu').click(function(){
		$(this).find('div').slideDown();
	});

	$('.accesslinkmenu').hover(function(){
		// hover
	},function(){
		$(this).find('div').slideUp();
	});


	$('.logmenu').click(function(){
		if ($(this).find('div').is(':visible'))
			$(this).find('div').slideUp('fast');
		else
			$(this).find('div').slideDown('fast');
	});

	$('.logmenu div').hover(function(){
		// hover
	},function(){
		$(this).slideUp();
	});

	$('.cancelbtnx').click(function(){
		gethref = $(this).attr('href');
		if ( $(this).parent().find('.rangebar').html()!=null)
		{
			var content = 'Goals - ';
			var getname = $(this).parent().find('span:first').html();
		}else{
			var getgrup = $(this).parents('.rightnav_content_new').find('h4').html();
			var getname = $(this).parent().find('input').val();
			var content = getgrup.replace(/<input[^>]*>/g,"");
			var content = content.replace(/<img[^>]*>/g,"");
			var content = content.replace(/(<a ([^<]+)<\/a>)/g,"");
			var content = content.replace("  ","");
		}

		var result = confirm("Delete "+content+": "+getname);
		if (result==true) {
			$.get(gethref,function(data){
				// callback deleted
			})

			$(this).parent().slideDown('fast',function(){
				$(this).remove();
			});
		}
	});


	$('.loginbox span').click(function(){
		if ( $(this).parent().hasClass('showverify') ){
			if ( $('.signupverify').is(":visible")){
				$('.signupverify').fadeOut('fast');
			}else{
				$('.signupverify').fadeIn('fast');
			}
		}else{
			if ( $(this).parent().find('form').is(":visible")){
				$('.loginbox').find('.logbox').fadeOut('fast');
			}else{
				parentelem = $(this).parent();
				$('.loginbox').not(parentelem).find('.logbox').fadeOut();
				$(this).parent().find('.logbox').fadeIn('fast');
			}
		}
	});

	$('.showverify').bind('click',function(){
			if ( $('.signupverify').is(":visible")){
				$('.signupverify').fadeOut('fast');
			}else{
				$('.signupverify').fadeIn('fast');
			}
	});

	$('.closelog, .btn_cancel, .btn_cancel2').bind('click',function(){
		$('header .logbox').fadeOut('fast');
		$('.contactbox').fadeOut('fast');
		$('.invitebox').fadeOut('fast');
		$('.signupverify').fadeOut('fast');
		$('.overlay').fadeOut()
		$('header .logbox').removeClass('show');
	});
	$('.loginbox').hover(function(){
		// hover
	},function(){
		//$(this).find('form').slideUp('fast');
	});

	$('.showlogin').click(function(){
			$('.invitebox').fadeOut('fast');
			$('.loginbox').eq(1).find('.logbox').fadeIn('fast');
	});




		if ( $('.slidingtxt').html()==null && $('section').html()!=null){
			offsetpage();
			////// Settings
			var scrollDirection = 0;
			$(window).scroll(function(event) {
				var scrollTop = $(this).scrollTop();
				var scrollBottom = $(this).height()+scrollTop;
				for (i=0;i<scrollAnimations.length;i++) {
					var c = scrollAnimations[i];
					if (c.start && scrollTop < c.start) continue;
					if (c.end && scrollTop > c.end) continue;
					if (c.condition && !c.condition(scrollTop, scrollBottom, scrollDirection)) continue;
					c.callback(scrollTop,scrollBottom,scrollDirection);
				}
				if ( $('.scrolldown').is(':visible') && !$('.scrolldown').is(':animated'))
					$('.scrolldown').animate({'opacity':0,'bottom':'-80px'},'fast',function(){
					var t=setTimeout(function(){ 
						$('.scrolldown').animate({'opacity':1,'bottom':'0'});
					},5000)
				});
			});
		}


	// WHY TALENTOMI
	if ( $('.slidingtxt section').html()!=null){
		getw = $(window).width();
		geth = $('.slidingtxt').height();
		$('.slidingtxt section').width(getw);
		$('.slidingtxt section').height(geth);
		$('.slidingtxt section').css({'position':'absolute'});
		starttxtslide = setInterval(autonextslide, 5000);
	}



	$('.headslide_txt .rightbracket').click(function(){

		if ( $('.slidingtxt section').is(':animated'))
		{
			//animating
		}else{
			clearInterval(starttxtslide);
			starttxtslide = 0;

				getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
				newindex = getindex+1;
				if ($('.slidingtxt section.active').next().html()!=null){
					//newindex=0;
					nextsliding(newindex);
				}

		}// animated


	});


	$('.headslide_txt .leftbracket').click(function(){

		if ( $('.slidingtxt section').is(':animated'))
		{
			//animating
		}else{

			clearInterval(starttxtslide);
			starttxtslide = 0;
			getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
			newindex = getindex-1;
			if ( $('.slidingtxt section.active').prev().html()!=null){
				//newindex= $('.slidingtxt section').size();
				//newindex--;
				prevsliding(newindex)
			}
		}

	});


	$('.bulletquote li').click(function(){
		if ( $(this).hasClass('active') ||  $('.slidingtxt section').is(':animated')) {
			//animating
		}else{
			clearInterval(starttxtslide);
			starttxtslide = 0;
			getindex = $('.bulletquote li').index( $(this) )
			oldindex = $('.bulletquote li').index( $('.bulletquote li.active') )
			
			if ( oldindex > getindex){
				prevsliding(getindex)
			}else{
				nextsliding(getindex)
				}
		}
		
	});


	$('.menu a.coming').hover(function(){
			$(this).find('em').stop().animate({'top':-40,'opacity':1})
	},function(){
			$(this).find('em').stop().animate({'top':-50,'opacity':0});
	})

	$('.rightnavslider .linkrmenu').click(function(){
		getid = $('.rightnavslider .linkrmenu').index( $(this));

		$('.rightnavslider .rightnav_content').not( '.rightnavslider .rightnav_content:eq('+getid+')' ).animate({'right':'-485px'},500);
		$('.rightnavslider .rightnav_content').eq(getid).animate({'right':'33px'},1000);
		$('.rightnav_content_grp').css({'width':'520px'});
	});

	$('.rightnav_content .arrback').click(function(){
		$('.rightnavslider .rightnav_content').animate({'right':'-485px'},500,function(){
			$('.rightnav_content_grp').css({'width':'0px'});
		});
	});

	$('.rateit p span').hover(function(){
		if ( $(this).hasClass('disabled')==false){
			$('.rateit p span').removeClass('active');
			getid = $(this).parent().find('span').index( $(this) );
			for(i=0;i<=getid;i++)
				$(this).parent().find('span').eq(i).addClass('active');
		}

	},function(){
		if ( $(this).hasClass('disabled')==false)
			$('.rateit p span').removeClass('active');
	})



	$('.rateit p span').bind(eventbtn,function(){
		if ( $(this).hasClass('disabled')==false){
			getid = $(this).parent().find('span').index( $(this) );
			getid++;
			$(this).parent().find('input[type=text]').val(getid);
			$(this).parent().attr('class','rate'+getid);
		}
	});	


	$('.startButton').click(function(){
		geturl = $(this).attr('rev');
		$('.btngrp').hide();
		  $.ajax({
			url:geturl,
			success:function(result){
				$('.question_message').hide()
				$('.questionform').html(result);
				$('.questionform').show();
					scrollerquest = $('.questionscroll').antiscroll().data('antiscroll');
				starttimer_assessment();
			  
			}
			});
	});
	

	$('.btn_keyinassessment').click(function(){
		geturl = $(this).attr('rev');
		$('.btngrp').hide();
		  $.ajax({
			url:geturl,
			success:function(result){
				$('.question_message').hide()
				$('.questionform').html(result);
				$('.questionform').show();
				getw = $('.questionscroll').width();
				//$('.questionscroll .antiscroll-inner').width(getw);
					scrollerquest = $('.questionscroll').antiscroll().data('antiscroll');
				

				//starttimer_assessment();
			  
			}
		});
	});
	
	$( "input[name=project_value]" ).unbind('keyup');
	$( "input[name=project_value]" ).bind( "keyup", function(e) {
		var getval = $(this).val();
		if( getval!='Project Value (Rupees)' && getval!= 'Project Value ($)')
			this.value = this.value.replace(/[^0-9\.]/g,'');
	});

	$( ".currency" ).unbind('keyup');
	$( ".currency" ).bind( "keyup", function(e) {
		var getval = $(this).val();
			this.value = this.value.replace(/[^0-9\.]/g,'');
	});

	if ( $('.verification_col2 select[name=status]').is(':disabled') ){
		$('.rateit p span').addClass('disabled');
		$('input[type="submit"]').attr('disabled','disabled');
		$('input[type="submit"]').css({opacity:0.5});

	}

	$('.validemail').unbind( "focusout");
	$('.validemail').bind( "focusout", function() {
		getval = $(this).val();
		var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;	
		if (!filter.test( getval )) {
			$(this).css({'background-color': '#fad0a8'});
		}else{
			$(this).css({'background-color': '#fff'});
		}

	})

	$('.questgrp .cancelbtnx').unbind( "click" );
	$('.questgrp .cancelbtnx').bind( "click", function() {
		geturl = $(this).attr('rev');
		getelem = $(this).parent();
		var r=confirm("Are you sure to delete");
		if (r){
		  $.ajax({
			url:geturl,
			success:function(result){
				getelem.remove();
			}});
		  }

	})


	$('.currency').currencyFormat();


	  $(".slidingtxt section").bind('touchstart', function(e){
	    down_x = e.originalEvent.touches[0].pageX;
	  });
	  $(".slidingtxt section").bind('touchmove', function(e){
	    e.preventDefault();
	    up_x = e.originalEvent.touches[0].pageX;
	  });
	  $(".slidingtxt section").bind('touchend', function(e){
	    touchdirection();
	  });


	$(".slidingtxt section").mousedown(function(e){
	    e.preventDefault();
	    down_x = e.pageX;
	  });
	 $(".slidingtxt section").mouseup(function(e){
	    up_x = e.pageX;
	    touchdirection();
	  });
	
	$('.playpause').click(function(){
		if ( $(this).hasClass('play')){
			$(this).removeClass('play');
			autoplay=true;
			clearInterval(starttxtslide);
			starttxtslide = 0;
			starttxtslide = setInterval(autonextslide, 5000);
		}else{
			$(this).addClass('play');
			autoplay=false;
		}
	});


		$('.tabsav li').unbind('click');
		$('.tabsav li').click(function(){
			if ( $(this).hasClass('active') ) {
				//animating
			}else{
				geti = $('.tabsav li').index( $(this) );
				$('.tabsav li').removeClass('active');
				$(this).addClass('active');
				$('.tabcontent').removeClass('active');

				gettop = $('.tabcontent').eq(geti).offset();
				$('body,html').animate({
					scrollTop: gettop.top
				},1000,'easeInOutQuad');
			}
			
		});


		if ($('.grid_heading').html()!=null){
			$('#contentlist > div:even').addClass('evencol');
			$('#contentlist2 > div:even').addClass('evencol');
		}
		$('.grid_heading').on('click', function () {
			if ( $(this).hasClass('up')==false &&  $(this).hasClass('disable')==false )
			{
					getindex = $(this).parent().find('.grid_heading').index( $(this) )
					getindex++;
				  $('#contentlist div.a_grid_col'+getindex).map(function () {
					return {val: $(this).text(), el: this.parentNode};
				  }).sort(function (a, b) {
					//return a.val - b.val ? 1 : -1;
					return a.val.toLowerCase() > b.val.toLowerCase() ? 1 : -1;  
				  }).map(function () {
					return this.el;
				  }).appendTo('#contentlist');
				  $(this).parent().find('.grid_heading').removeClass('up');
				  $(this).parent().find('.grid_heading2').removeClass('down');
				  $(this).addClass('up');
				  $('#contentlist > div').removeClass('evencol');
				  $('#contentlist > div:even').addClass('evencol');
			}else if ( $(this).hasClass('up') &&  $(this).hasClass('disable')==false )
			{
					getindex = $(this).parent().find('.grid_heading').index( $(this) )
					getindex++;
				  $('#contentlist div.a_grid_col'+getindex).map(function () {
					return {val: $(this).text(), el: this.parentNode};
				  }).sort(function (a, b) {
					//return a.val - b.val ? 1 : -1;
					return a.val.toLowerCase() < b.val.toLowerCase() ? 1 : -1;  
				  }).map(function () {
					return this.el;
				  }).appendTo('#contentlist');
				  $(this).parent().find('.grid_heading').removeClass('up');
				  $(this).parent().find('.grid_heading2').removeClass('down');
				  $(this).addClass('up');
				  $('#contentlist > div').removeClass('evencol');
				  $('#contentlist > div:even').addClass('evencol');
			}
		});


		$('.grid_heading2').on('click', function () {
			if ( $(this).hasClass('up')==false &&  $(this).hasClass('disable')==false )
			{
					getindex = $(this).parent().find('.grid_heading2').index( $(this) )
					getindex++;
				  $('#contentlist2 div.v_grid_col'+getindex).map(function () {
					return {val: $(this).text(), el: this.parentNode};
				  }).sort(function (a, b) {
					//return a.val - b.val ? 1 : -1;
					if ( isNaN( a.val ) || isNaN( b.val ) ){
						return a.val.toLowerCase() > b.val.toLowerCase() ? 1 : -1;  
					}else{
						return parseInt(a.val) > parseInt(b.val) ? 1 : -1;  
					}
				  }).map(function () {
					return this.el;
				  }).appendTo('#contentlist2');
				  $(this).parent().find('.grid_heading2').removeClass('up');
				  $(this).parent().find('.grid_heading2').removeClass('down');
				  $(this).addClass('up');
				  $('#contentlist2 > div').removeClass('evencol');
				  $('#contentlist2 > div:even').addClass('evencol');
			}else if ( $(this).hasClass('up') &&  $(this).hasClass('disable')==false )
			{
					getindex = $(this).parent().find('.grid_heading2').index( $(this) )
					getindex++;
				  $('#contentlist2 div.v_grid_col'+getindex).map(function () {
					return {val: $(this).text(), el: this.parentNode};
				  }).sort(function (a, b) {
					//return a.val - b.val ? 1 : -1;
					if ( isNaN( a.val ) || isNaN( b.val ) ){
						return a.val.toLowerCase() < b.val.toLowerCase() ? 1 : -1;  
					}else{
						return parseInt(a.val) < parseInt(b.val) ? 1 : -1;  
					}
				  }).map(function () {
					return this.el;
				  }).appendTo('#contentlist2');
				  $(this).parent().find('.grid_heading2').removeClass('up');
				  $(this).parent().find('.grid_heading2').removeClass('down');
				  $(this).addClass('down');
				  $('#contentlist2 > div').removeClass('evencol');
				  $('#contentlist2 > div:even').addClass('evencol');
			}
		});

		
		if ($('.searchfilter a').html()!=null){
			getindex = $('.searchfilter a').index( $('.searchfilter a.active') );
			if (getindex==0){
				$('#assesssmentlist').next().show();
					$('#candidatelist').next().hide();
			}else{
					$('#assesssmentlist').next().hide();
					$('#candidatelist').next().show();
			}
		}
		$('.searchfilter a').on('click', function () {
			if ( $(this).hasClass('active')==false){
				$('.searchfilter a').removeClass('active');
				$(this).addClass('active');
				if ( $(this).html()=='Assessment'){
					$('#assesssmentlist').next().show();
					$('#candidatelist').next().hide();
					$('.wrapper_col2 .contentbox2 .grid_heading4').html('Candidate Assigned');
				}
				if ( $(this).html()=='Candidate'){
					$('#assesssmentlist').next().hide();
					$('#candidatelist').next().show();
					$('.wrapper_col2 .contentbox2 .grid_heading4').html('Assessment Assigned');
				}
			}
		});


		$('.forgotpassword').on('click', function () {
			//$('.logbox').not('.forgotpop').fadeOut('fast');
			$('.forgotpop').fadeIn();
		});

		$('.btn_login2').on('click', function () {
			$('.logbox').fadeOut('fast');
			$('.logbox').eq(1).fadeIn();
		});

		$('.showchangepwd').on('click', function () {
			$('.logbox').fadeOut('fast');
			$('.resetpw').fadeIn();
		});

		$('.contact').on('click', function () {
			$('.logbox').fadeOut('fast');
			$('.contactbox').fadeIn();
					$('.contact_col1:first').show();
					$('.contact_col1.noshow').hide();

		});


	$('.compressmenus > ul li span').bind('click',function(){
		if ( $(this).find('ul').is(':hidden')){
			$(this).find('ul').slideDown('fast');
		}else{
			$(this).find('ul').slideUp('fast');
		}
	});


	$('input[name=calc_submit]').bind('click',function(){
		checkvalid=true;
		if (checkvalid){
			var noofhire = $('#hires').val() ;
			var timetohire = $('#timetohire').val();
			var refhire = $('#referralhire').val() / 100;
			var hireaccept = $('#hireoffer').val() / 100;
			var typeofhire = $('#typeofhire').val();
			var hours_per_hire =  (120)/ ( refhire );
			var total_view_hrs =((noofhire*hours_per_hire*refhire)/hireaccept)*typeofhire;
			var total_costhire = total_view_hrs*100;
			$('.home5_col3 span:first').html(total_view_hrs);
			$('.home5_col3 span:last').html("$"+total_costhire);
		}

	});


		$('#calculatehire input[type=text]').keydown(function(event) {
                // Allow special chars + arrows 
                if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 
                    || event.keyCode == 27 || event.keyCode == 13 
                    || (event.keyCode == 65 && event.ctrlKey === true) 
                    || (event.keyCode >= 35 && event.keyCode <= 39)){
                        return;
                }else {
                    // If it's not a number stop the keypress
                    if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105 )) {
                        event.preventDefault(); 
                    }   
                }
            });



	if ( $('.sectionslider').html()!=null)
		globalslider();

	$('.slider1_next').click(function(){
	if ( $('.slider1_box .sliderthumbs').is(':animated')){
			// animating
		}else{	
			var getn = $('.slider1_next').index($(this));
			var getactive = $('.sectionslider').eq(getn).find('.slider1_box .sliderthumbs').index( $('.sectionslider').eq(getn).find('.slider1_box .sliderthumbs.active') ); 
			getactive++;
			if ( $('.sectionslider').eq(getn).find('.slider1_box .sliderthumbs').eq(getactive).html()!=null){
				nextsliding_arr(getactive, getn);
			}
		}

	})

	$('.slider1_prev').click(function(){
		if ( $('.slider1_box .sliderthumbs').is(':animated')){
			// animating
		}else{
			var getn = $('.slider1_prev').index($(this));
			var getactive = $('.sectionslider').eq(getn).find('.slider1_box .sliderthumbs').index( $('.sectionslider').eq(getn).find('.slider1_box .sliderthumbs.active') ); 
			getactive--;
			if ( getactive>=0){
				prevsliding_arr(getactive, getn);
			}
		}

	})




// END DOC
});





function globalslider(){
	var totalslider = $('.sectionslider').size();
	geth_arr = new Array();
	setTimeout( function(){ 	
		for(i=0;i<totalslider;i++){
			geth_arr[i] = $('.sectionslider').eq(i).width()-140;
			$('.sectionslider').eq(i).find('.slider1_box').width(geth_arr[i]);
			$('.sectionslider').eq(i).find('.slider1_box .sliderthumbs').width(geth_arr[i]-2);

			$('.sectionslider').eq(i).find('.slider1_box .sliderthumbs').css({'left': geth_arr[i]+"px"});
			$('.sectionslider').eq(i).find('.slider1_box .sliderthumbs.active').css({'left': "0px"});
			//col1_element  = $('.col1_txt').eq(i);
			//autonextslide_global( col1_element ); 
	}
	}, 500);
}


function nextsliding_arr(newindex, geti){
		getw = $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').width()+2;
		//$('.col1_txt').eq(geti).css({'width':getw})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').eq(newindex).css({'left':getw+'px','display':'block'})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs.active').stop().animate({'left':-getw+'px'},1000,'easeInOutQuad',function(){
			$(this).removeClass('active')
		})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').eq(newindex).stop().animate({'left':'0px'},1000,'easeInOutQuad',function(){
			$(this).addClass('active')
			//clearInterval(starttxtslide_arr[geti]);
			//starttxtslide_arr[geti] = 0;			
		})
}

function prevsliding_arr(newindex, geti){
		getw = $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').width()+2;
		//$('.col1_txt').eq(geti).css({'width':getw})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').eq(newindex).css({'left':-getw+'px','display':'block'})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs.active').stop().animate({'left':getw+'px'},1000,'easeInOutQuad',function(){
			$(this).removeClass('active')
		})
		 $('.sectionslider').eq(geti).find('.slider1_box .sliderthumbs').eq(newindex).stop().animate({'left':'0px'},1000,'easeInOutQuad',function(){
			$(this).addClass('active')
			//clearInterval(starttxtslide_arr[geti]);
			//starttxtslide_arr[geti] = 0;			
		})
}




function checkagree(){
	var atLeastOneIsChecked = $('.forcheckbox :checkbox:checked').length > 0;
	if ( atLeastOneIsChecked<=0 ){
		$('.forcheckbox').css({'color':'#cc0000'});
		return false;
	}
	return true;
}

function touchdirection()
{
  if ((down_x - up_x) > 50)
    {
        slide_right();
    }
    if ((up_x - down_x) > 50)
	    {
        slide_left();
    }
}




function slide_left(){
		if ( $('.slidingtxt section').is(':animated'))
		{
			//animating
		}else{

			clearInterval(starttxtslide);
			starttxtslide = 0;
			getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
			newindex = getindex-1;
			if ( $('.slidingtxt section.active').prev().html()!=null){
				prevsliding(newindex)
			}
		}

}




function slide_right(){

		if ( $('.slidingtxt section').is(':animated'))
		{
			//animating
		}else{
			clearInterval(starttxtslide);
			starttxtslide = 0;

				getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
				newindex = getindex+1;
				if ($('.slidingtxt section.active').next().html()!=null){
					//newindex=0;
					nextsliding(newindex);
				}

		}// animated


}




function nextsliding(newindex){
	
			getw = $('.slidingtxt').width();
				$('.bulletquote li').removeClass('active');
				$('.bulletquote li').eq(newindex).addClass('active');
				//$('.slidingtxt').stop().animate({'width':'619px'},1500,'easeInOutQuad')
				//$('.headslide_txt').stop().animate({'width':'650px'},1500,'easeInOutQuad')
				getw= $(window).width();
				$('.slidingtxt section').eq(newindex).css({'left':getw+'px','display':'block'})
				$('.slidingtxt section.active').stop().animate({'left':-getw+'px'},1500,'easeInOutQuad',function(){
					$(this).removeClass('active')
				})
				$('.slidingtxt section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
					$(this).addClass('active')
					$('.leftbracket').removeClass('disable');
					if ($(this).next().html()==null)
						$('.rightbracket').addClass('disable');
					else
						$('.rightbracket').removeClass('disable');

					clearInterval(starttxtslide);
					starttxtslide = 0;
					starttxtslide = setInterval(autonextslide, 5000);
				})
}

function prevsliding(newindex){
			
			getw = $('.slidingtxt').width();
			//$('.slidingtxt').stop().animate({'width':'619px'},1500,'easeInOutQuad')
			//$('.headslide_txt').stop().animate({'width':'650px'},1500,'easeInOutQuad')
			getw= $(window).width();
			$('.bulletquote li').removeClass('active');
			$('.bulletquote li').eq(newindex).addClass('active');
			$('.slidingtxt section').eq(newindex).css({'left':-getw+'px','display':'block'})
			$('.slidingtxt section.active').stop().animate({'left':getw+'px'},1500,'easeInOutQuad',function(){
				$(this).removeClass('active');
			})
			$('.slidingtxt section').eq(newindex).stop().animate({'left':'0px'},1500,'easeInOutQuad',function(){
				$(this).addClass('active');
				$('.rightbracket').removeClass('disable');
				if ($(this).prev().html()==null)
					$('.leftbracket').addClass('disable');
					clearInterval(starttxtslide);
					starttxtslide = 0;
				starttxtslide = setInterval(autonextslide, 5000);
			})
}


function autonextslide(){
					clearInterval(starttxtslide);
					starttxtslide = 0;
				getindex = $('.slidingtxt section').index( $('.slidingtxt section.active') );
				newindex = getindex+1;
				if ($('.slidingtxt section.active').next().html()!=null && autoplay ){
					nextsliding(newindex);
				}else if ($('.slidingtxt section.active').next().html()==null && autoplay ){
					nextsliding(0);
				}
}


window.onresize = function(event) {
	//reloadtop();
}

function reloadtop(){
		geth = $(window).height();
		getheader =  $('header').outerHeight(true);
		geth = geth - getheader;




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


(function($) {
        $.fn.currencyFormat = function() {
            this.each( function( i ) {
                $(this).change( function( e ){
                    if( isNaN( parseFloat( this.value ) ) ) return;
                    this.value = parseFloat(this.value).toFixed(2);
                });
            });
            return this; //for chaining
        }
 })( jQuery );


function showpop(geturl){
	
	$('.overlay').fadeIn()
	$('.popup').fadeIn();
	$('.popup .copyform').html('')
	$.get(geturl,function(data){
		$('.popup .copyform').html(data);
		var geth = $('.popup .copyform').height();
		var getw = $('.popup .copyform').width();
		if( $('.popup .copyform .answerlist_sel').html()!=null){
			geth=geth+200;
		}

		if( $('.popup .copyform .languagefield').html()!=null ){
			geth=geth+80;
		}
			$('.popup').height(geth)
			$('.popup').width(getw)
			$('.closepop').unbind('click');
			$('.closepop').bind('click',function(){
				$('.overlay').fadeOut()
				$('.popup').fadeOut()
				if ($(this).find('.cancelButton').html()==null) {
					$('.rightnavslider .rightnav_content').animate({'right':'-485px'},500,function(){
						$('.rightnav_content_grp').css({'width':'0px'});
					});
				}
			});

		if( $('.popup .copyform #id_assessTime').val()!=null){
			$('#id_assessTime').timepicker();
		}

			if ( $('label.label_check').html()!=null ){
				for(i=0;i< $('label.label_check').size(); i++){
					($('label.label_check').eq(i).find('input[type=checkbox]').is(':checked')) ? $('label.label_check').eq(i).addClass('label_check c_on') : $('label.label_check').eq(i).addClass('label_check c_off');							
				}
				$('label.label_check').unbind('click');
				$('label.label_check').bind('click',function(e){
					e.stopPropagation();
					e.preventDefault();
					if ( $(this).hasClass('c_on')){
						$(this).removeClass('c_on');
						$(this).addClass('c_off');
						$(this).find('input[type=checkbox]').attr('checked',false);
					}else{
						$(this).addClass('c_on');
						$(this).removeClass('c_off');
						$(this).find('input[type=checkbox]').attr('checked',true);
					}

				});

			}

	
		$( "input[name=project_value]" ).unbind('keyup');
		$( "input[name=project_value]" ).bind( "keyup", function(e) {
			var getval = $(this).val();
			if( getval!='Project Value (Rupees)' && getval!= 'Project Value ($)')
				this.value = this.value.replace(/[^0-9\.]/g,'');
		});

		$( ".currency" ).unbind('keyup');
		$( ".currency" ).bind( "keyup", function(e) {
			var getval = $(this).val();
				this.value = this.value.replace(/[^0-9\.]/g,'');
		});

		if ( $('.verification_col2 select[name=status]').is(':disabled') ){
			$('.rateit p span').addClass('disabled');
			$('input[type="submit"]').attr('disabled','disabled');
			$('input[type="submit"]').css({opacity:0.5});

		}

		$('.validemail').unbind( "focusout");
		$('.validemail').bind( "focusout", function() {
			getval = $(this).val();
			var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;	
			if (!filter.test( getval )) {
				$(this).css({'background-color': '#fad0a8'});
			}else{
				$(this).css({'background-color': '#fff'});
			}

		})

		$('.questgrp .cancelbtnx').unbind( "click" );
		$('.questgrp .cancelbtnx').bind( "click", function() {
			geturl = $(this).attr('rev');
			getelem = $(this).parent();
			var r=confirm("Are you sure to delete");
			if (r){
			  $.ajax({
				url:geturl,
				success:function(result){
					getelem.remove();
				}});
			  }

		})


	})
}



function offsetpage(){
	/*if(sechomeH < videohomeH){
		$('section#home').height(videohomeH);
	}*/
    hwindow = window.innerHeight;
    scrollTopres = $(window).scrollTop();

    var offsettxt1 = $('#home_1 div').offset();
    /*var offsettxt2 = $('#home_2 div').offset();
    var offsettxt3 = $('#home_3 div').offset();
    var offsettxt4 = $('#home_4 div').offset();*/
    var offsettxt5 = $('#home_5 div').offset();
    var offsettxt6 = $('#home_6 div').offset();

    scrollAnimations = [];

	var offseth = $('#home').offset();
    var scrollBottomh = $('#home').height()+offseth.top+50 ;
    var offsetm = $('#home_1').offset();
    scrollAnimations.push({
        'start': 0,
        'end': scrollBottomh+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){

				if ( $(window).height() > 540 ){
					//$('#home').css('background-position', '0px ' + -(scrollTop-offseth.top-35)*0.3+'px');
				}else{
					//$('#home').css('background-position', '50% ' + -(scrollTop-offseth.top-35)*0.3+'px');
				}

		}
    });



    var scrollBottomm = $('#home_1').height()+offsetm.top+50 ;
	scrollAnimations.push({
        'start': offsetm.top - 75,
        'end': scrollBottomm+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){

			$('.scrolldown').show();
			 if (offsetm.top < scrollTop && (offsetm.top+330) > scrollTop){
				 var gett = scrollTop - offsetm.top;
				 //$('#home_1 div').html( gett+"=="+(offsettxt1.top - offsetm.top));
				 $('#home_1 div').css('top',  (gett+(offsettxt1.top - offsetm.top))+'px');
			 }

	   }
    });

/*
    var offseta = $('#home_2').offset();
    var scrollBottoma = $('#home_2').height()+offseta.top ;
	scrollAnimations.push({
        'start': offseta.top - 75,
        'end': scrollBottoma+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){

			$('.scrolldown').show();
			 if (offseta.top < scrollTop && (offseta.top+400) > scrollTop){
				 var gett = scrollTop - offseta.top;
				 $('#home_2 div').css('top',  (gett+(offsettxt2.top - offseta.top))+'px');
			 }

	   }
    });


    var offsetc = $('#home_3').offset();
    var scrollBottomc = $('#home_3').height()+offsetc.top ;
	scrollAnimations.push({
        'start': offsetc.top - 75,
        'end': scrollBottomc+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){

			$('.scrolldown').show();
			 if (offsetc.top < scrollTop && (offsetc.top+400) > scrollTop){
				 var gett = scrollTop - offsetc.top;
				 $('#home_3 div').css('top',  (gett+(offsettxt3.top - offsetc.top))+'px');
			 }

	   }
    });



    var offsetd = $('#home_4').offset();
    var scrollBottomd = $('#home_4').height()+offsetd.top ;
	scrollAnimations.push({
        'start': offsetd.top - 75,
        'end': scrollBottomd+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){
			$('.scrolldown').show();

			 if (offsetd.top < scrollTop && (offsetd.top+450) > scrollTop){
				 var gett = scrollTop - offsetd.top;
				 $('#home_4 div').css('top',  (gett+(offsettxt4.top - offsetd.top))+'px');
			 }

	   }
    });
*/


    var offsete = $('#home_5').offset();
    var scrollBottome = $('#home_5').height()+offsete.top ;
	scrollAnimations.push({
        'start': offsete.top - 75,
        'end': scrollBottome+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){

			 if (offsete.top < scrollTop && (offsete.top+280) > scrollTop){
				 var gett = scrollTop - offsete.top;
				 $('#home_5 > div').css('top',  (gett+(offsettxt5.top - offsete.top))+'px');
			 }

			 $('.scrolldown').show();

	   }
    });




    var offsetf = $('#home_6').offset();
    var scrollBottomf = $('#home_6').height()+offsetf.top ;
	scrollAnimations.push({
        'start': offsetf.top - 75,
        'end': scrollBottomf+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){
			$('.scrolldown').hide();

			 if (offsetf.top < scrollTop && (offsetf.top+350) > scrollTop){
				 var gett = scrollTop - offsetf.top;
				 $('#home_6 div').css('top',  (gett+(offsettxt6.top - offsetf.top))+'px');
			 }

	   }
    });

  /*  var scrollBottomsu = $('#home_4').height()+offsetcont.top+70 ;
    scrollAnimations.push({
        'start': offsetcont.top - 120,
        'end': scrollBottomsu+hwindow,
        'callback': function(scrollTop,scrollBottom,scrollDirection){
            $('#home_4').css('background-position', '50% ' + -(scrollTop-offsetcont.top)*0.3+'px');

       }
    });
	*/

}

var totalSeconds = 1800;
function starttimer_assessment(){
        setInterval(setTime, 1000);
}

function setTime()
{
	totalSeconds--;
	if (totalSeconds>=0)
		$('.timer span').html( pad(parseInt(totalSeconds/60)) +":"+ pad( totalSeconds%60) );
	else
		document.assessment.submit();
}

function pad(val)
{
	var valString = val + "";
	if(valString.length < 2){
		return "0" + valString;
	}
	else{
		return valString;
	}
}



function checklogin(){
  var checkvalidate = true;

	getval = $('#logbox input[name=emailid]').val();
	var filter = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;	
	if (!filter.test( getval )) {
	     alert( "Please Enter valid Email" );
		$('#logbox input[name=emailid]').css({'background-color': '#fad0a8'});
		checkvalidate=false;
	}else{
		$('#logbox input[name=emailid]').css({'background-color': '#fff'});
	}

  if( $('#logbox input[name=password]').val() == "" || $('#logbox input[name=password]').val() == "password" )
   {
     checkvalidate =  false;
     alert( "Please Enter password" );
     $('#logbox input[name=password]').css({'background-color': '#fad0a8'});
	 return false;
   }

	return checkvalidate;
}