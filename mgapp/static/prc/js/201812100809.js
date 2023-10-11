
$J(document).ready(function(){
    //GNB ***************************************
        var gnbPcBg = $J('.gnb_bg');
        var gnb1st = $J('.gnb > ul > li > a');	// for mobile
        var gnb2nd = $J('.gnb > ul > li > ul');	// for pc
        var WinSize = $J(window).width();
        var bodyHeight = $J('#wrap').outerHeight()+50;
        var mobilePoint = 768;
        var isMobile;	// for disable GNB showing
        var tab1Li = $J('.tab1 ul li');
        var tab1Len = tab1Li.length;
        var tab2Li = $J('.tab2 ul li');
        var tab2Len = tab2Li.length;	
        var gnbBgHeight = 0; // GNB �믪씠 �먮룞議곗젅
        setIsMobile();
        $zoom();
        srchWrap2InputSize(); // S01	
        $J('.gnb > ul > li > a, .gnb_bg').on('mouseenter',function(){
            showPcGnb();
        });
        $J('.global, .container-e, .container-w').on('mouseenter',function(){
            hidePcGnb();
        });
        $J('.header .gnb_wrap .gnb > ul > li:first-child > a').focus(function(){
            showPcGnb();
        }).keydown(function(event){
            var keycode = event.keyCode;
            if (keycode === 9) {
                if(event.shiftKey){
                    event.stopPropagation();
                    hidePcGnb();
                }else{
                    event.stopPropagation();
                    showPcGnb();
                }	    
            }
        });
        $J('.header .gnb_wrap .gnb > ul > li:last-child > ul > li:last-child > a').keydown(function(event){
            var keycode = event.keyCode;
            if (keycode === 9) {			
                event.stopPropagation();
                hidePcGnb();
            }
            //$J('#container').focus(); // �묎렐�깆삤瑜�
            $J('.container').focus();// �묎렐�깆옉��
        });
        $J(gnb1st).on('click',function(){ // 1�곸뒪�대┃	
            // 湲곗뾽�� 
            if($J('.header-w').length){
                if($J(this).next().is(':visible') && isMobile) {
                    $J(this).next().slideUp('fast');
                }else {
                    $J(this).next().slideDown('fast');
                }
            }	
            // etk 
            if($J('.header-e').length){
                if($J('.gnb_bg').is(':visible')){
                    hideGnb();
                    //console.log($J('.gnb_bg').is(':visible'));
                }else{
                    showGnb();
                    //console.log($J('.gnb_bg').is(':visible'));
                }
            }		
        });
        function showGnb(){ // only for ETK
            gnbBgHeightAuto();
            gnbPcBg.show();
            gnb2nd.show();
        }
        function hideGnb(){ // only for ETK
            gnbPcBg.hide();
            gnb2nd.hide();
        }
        function showPcGnb(){
            if(!isMobile) {
                gnbPcBg.show();
                gnb2nd.show();
                //if($J('.srch_area').is(':visible')){srchBoxClose();}
            }
        }
        function hidePcGnb(){
            if(!isMobile) {
                gnbPcBg.hide();
                gnb2nd.hide();
            }
        }
        function setIsMobile(){
            if(WinSize > mobilePoint){
                isMobile = false;
                hidePcGnb();
                //$J('.gnb').css({'left':200,'opacity':1});
                //$J('.header-w.en .gnb').css({'left':300,'opacity':1});
                //$J('.header-e.en .gnb').css({'left':300,'opacity':1}); // etn_en gnb 醫뚯륫�щ갚
                $J('.menu-toggle').removeClass('is-active');
                
                if($J('.header-w .gnb').hasClass('cn') || $J('.header-w .gnb').hasClass('tw') || $J('.header-w .gnb').hasClass('ja')){
                    $J('.header-w .gnb').css('left','230px');
                } else if($J('.header-e .gnb').hasClass('cn') || $J('.header-e .gnb').hasClass('tw') || $J('.header-e .gnb').hasClass('ja')){
                    $J('.header-e .gnb').css('left','260px');
                } else {
                    $J('.header-w .gnb').css('left','200px');
                }
                
                $J('.ham_bg').hide();
                srchBoxOpen();
                tab1ResizeForPc();
                gnbBgHeightAuto();
            }else{
                if(isMobile == false){ // mobilePoint 蹂��� �쒖젏留� �묐룞�쒕떎.
                    srchBoxClose();				
                }
                isMobile = true;
                showPcGnb();
                if($J('.header-w').length){
                    tab1ResizeForMobile();
                    tab2ResizeForMobile();
                    gnbBgHeightRollBack();
                }
                if($J('.menu-toggle').hasClass('is-active')){				
                }else{
                    //hamClose2();
                    $J('.header-w .gnb').css('left','-100%'); // pc �먯꽌 mobile 吏꾩엯(resize)�� �꾨쾭嫄곌� left 200 利앹긽.
                }
            }
            if($J('.header-w').length){			
                $J('.ham_bg').css('height',bodyHeight); // �꾨쾭嫄� 2�곸뒪媛� 臾댁벝紐� 湲몄뼱吏�
            }
            $J('.gnb').css({'opacity': '1'}); // �꾨쾭嫄� on off �� pc 由ъ궗�댁쫰 �� 硫붾돱 �뚰뙆 0.4 利앹긽.
        }
    // GNB �믪씠 �먮룞議곗젅 ***************************************
        function gnbBgHeightAuto(){
            $J('.header .gnb_wrap .gnb > ul > li').each(function(){
                //console.log($J(this).children('ul').height());
                if($J(this).children('ul').height() > gnbBgHeight){
                    gnbBgHeight = $J(this).children('ul').height();
                }
            });
            $J('.gnb_bg').css('height',gnbBgHeight + 50);
            $J('.header .gnb_wrap .gnb > ul > li > ul').css('height',gnbBgHeight);
        }
        function gnbBgHeightRollBack(){
            $J('.gnb_bg').css('height','auto');
            $J('.header .gnb_wrap .gnb > ul > li > ul').css('height','auto');
        }
    
    // 由ъ궗�댁쭠 ***************************************
        $J( window ).on('resize', function() {
            WinSize = $J( window ).width();
            setIsMobile();
            if($J('.menu-toggle').hasClass('is-active')){
                //hamClose(); // 由ъ궗�댁쫰 �� �ロ옒 = 紐⑤컮�� �꾨쾭嫄� 硫붾돱 3�곸뒪 �쇱묠 �곹깭�먯꽌 �ㅼ��댄븨 �� �꾨쾭嫄� �ロ옒
            }
            //viewTrHeight(); // view�섏씠吏� �� �믪씠 源⑥��� �ㅻ쪟
            srchWrap2InputSize(); // S01
        });
        
        
    
    // �꾨쾭嫄� �쇱묠 ***************************************
        $J('.menu-toggle').on('click',function(){
            if($J(this).hasClass('is-active')){
                hamClose();
            }else{
                hamOpen();
            }
        });
        function hamClose(){
            $J('.gnb').animate({ left: '-100%', opacity: 0.4},400,'easeInQuart');
            $J('.header .gnb_wrap .gnb > ul > li > ul').delay(200).slideUp();
            $J('.menu-toggle').children().text('硫붾돱�닿린');
            $J('.ham_bg').fadeOut('fast');
            $J('.menu-toggle').removeClass('is-active');
        }
        function hamClose2(){ // �좊땲硫붿씠�� �녿뒗 踰꾩쟾.
            $J('.gnb').css({ left: '-100%'});
            $J('.header .gnb_wrap .gnb > ul > li > ul').hide();
            $J('.menu-toggle').children().text('硫붾돱�닿린');
            $J('.ham_bg').hide();
            $J('.menu-toggle').removeClass('is-active');
        }
        function hamOpen(){
            $J('.gnb').animate({left: 0, opacity: 1},150,'easeInQuart');
            $J('.menu-toggle').children().text('硫붾돱�リ린');
            $J('.ham_bg').fadeIn('fast');
            $J('.menu-toggle').addClass('is-active');
        }
        $J('#wrap').prepend('<div class="ham_bg"></div>');
        
    
    //gnb 寃��� �쇱묠 ***************************************
        $J('.srch_btn_global').on('click',function(){
            if($J('.srch_area').is(':visible')){
                srchBoxClose();
            }else {			
                srchBoxOpen();
            }
        });
        function srchBoxOpen(){
            if(gnb2nd.is(':visible')){hidePcGnb();}
            $J('.srch_area').slideDown('fast');			
            $J('.srch_btn_global').children().attr('alt','寃��됰컯�� �リ린');
            //$J('.srch_input').focus();
        }
        function srchBoxClose(){
            if(!$J('.container-e').length){
                $J('.srch_area').hide();
                $J('.srch_btn_global').children().attr('alt','寃��됰컯�� �닿린');
            }
        }
        //寃���
        var srchMenuListTemp = $J('.srch_result').html();	
        $J('.srch_input').on('keyup',function(e){
            var keycode = e.keyCode;
            if(keycode == 13){$J('.srch_go').trigger('click');}
        });
        $J('.srch_go').on('click',function(){
            var typeIn = String($J('.srch_input').val());	
            $J('.srch_result').html(srchMenuListTemp);
            $J('.srch_result a').each(function(){
                var menuTxt =  String($J(this).html());
                $J(this).html($J(this).html());			
                if(menuTxt.indexOf(typeIn) >= 0 && typeIn !== ""){				
                    $J(this).parent().show();
                    $J(this).html($J(this).html().replace(typeIn,'<span class="match">'+typeIn+'</span>'));
                }else{
                    $J(this).parent().hide();
                }
            });
            if($J('.srch_result li').is(':visible')){
                $J('.srch_result_close').show();
                $J('.srch_result').css('border','1px solid #dee2eb');
            }else{
                $J('.srch_result').css('border','0');
            }
        });
        //寃��됰━�ㅽ듃 吏��곌린
        /*$J('body').on('click','.srch_result_close',function(){
            $J('.srch_input').val('');
            $J('.srch_go').trigger('click');
        });*/
        //寃��됰━�ㅽ듃 �リ린
        $J('.container').on('click',function(){
            $J('.srch_input').val('');
            $J('.srch_go').trigger('click');
        });
        //gnb �쇱묠 under-bar
        $J('.header-w .gnb_wrap .gnb > ul > li').hover(function(){
            if(!isMobile) $J(this).children('a').css('border-bottom','3px solid #c7187d');
        },function(){
            $J(this).children('a').css('border-bottom','0');
        });
        $J('.header-e .gnb_wrap .gnb > ul > li').hover(function(){
            if(!isMobile) $J(this).children('a').css('border-bottom','3px solid #883d7c');
        },function(){
            $J(this).children('a').css('border-bottom','0');
        });
        
    // gnb 1depth �덈퉬 議곗젙 ***************************************	
        var gnbLength = $J('.gnb > ul > li').length;
        /* if(!isMobile) {
            if(gnbLength == 3){
                $J('.gnb > ul > li').css('width','260px');
            }else if(gnbLength == 4){
                $J('.gnb > ul > li').css('width','220px');
                $J('.gnb').css('left','230px');
            }else if(gnbLength == 5){
                $J('.gnb > ul > li').css('width','186px');
                $J('.gnb').css('left','200px');
            }
        } */
    
    // etk 硫붿씤 �꾩씠肄� 濡ㅼ삤踰� ***************************************
        $J('.container-e .content_l .quick li a').hover(function(){
            $J('.container-e .content_l .quick li').eq(0).find('img').attr('src',function(i, src){
                return src.replace('_on.png','.png');
            });
            $J(this).find('img').attr('src',function(i, src){
                return src.replace('.png','_on.png');
            });
        },function(){
            $J(this).find('img').attr('src',function(i, src){
                return src.replace('_on.png','.png');
            });
            $J('.container-e .content_l .quick li').eq(0).find('img').attr('src',function(i, src){
                return src.replace('.png','_on.png');
            });
        });
    
    // dropdown menu ***************************************
        $J( ".dropdown1" ).selectmenu();
        $J( ".dropdown2" ).selectmenu().selectmenu( "menuWidget" ).addClass( "overflow" );
        $J( ".dropdown3" ).selectmenu().selectmenu( "menuWidget" ).addClass( "overflow" );
        $J( ".dropdown_f" ).selectmenu({
            icons: { button: "ui-icon-circle-triangle-s" }
        });
        $J( ".dropdown_f2" ).selectmenu({
            icons: { button: "ui-icon-circle-triangle-s" }
        });
    
        // �곷떒 language �쒕∼諛뺤뒪 �대룞踰꾪듉
        //$J('.topmovebtn').attr('href',$J('#dynamic_select option').eq(0).val()); // language �듭뀡�� �놁쓣 寃쎌슦 泥ル쾲吏� �듭뀡媛믪쓣 �대룞踰꾪듉 �대뒗��.
        $J('#dynamic_select').selectmenu({
            change: function() {
                if($J(this).val() != '') {
                    $J('.topmovebtn').attr('href',$J(this).val());
                    //window.location = $J(this).val();
                }
            }
        });
    
        // �곷떒 language �쒕∼諛뺤뒪 �대룞踰꾪듉 2nd(援�린�쒖떆)
        $J.widget( "custom.iconselectmenu", $J.ui.selectmenu, {
            _renderItem: function( ul, item ) {
                var li = $J( "<li>" ),
                wrapper = $J( "<div>", { text: item.label } );
                if ( item.disabled ) {
                    li.addClass( "ui-state-disabled" );
            }
            $J( "<span>", {
                    style: item.element.attr( "data-style" ),
                    "class": "ui-icon " + item.element.attr( "data-class" )
                }).appendTo( wrapper );
                return li.append( wrapper ).appendTo( ul );
            }
        });
        $J( "#dynamic_select2" )
        .iconselectmenu({
            change: function() {
                if($J(this).val() != '') {
                    $J('.topmovebtn').attr('href',$J(this).val());
                    //window.location = $J(this).val();
                }
            }
        })
        .iconselectmenu( "menuWidget" )
        .addClass( "ui-menu-icons customicons" );
        // �곷떒 湲�濡쒕쾶硫붾돱+���吏� �붾뱾由щ뒗 �꾩긽
        setTimeout( function(){
            $J('.login_wrap').css('visibility','visible');
        }, 500 );
    
    
        
        
        // �명꽣 �좉�湲곌� �쒕∼諛뺤뒪 �대룞踰꾪듉
        $J('#dynamic_footer_select').selectmenu({
            change: function() {
                if($J(this).val() != '') {
                    $J('.bottomMoveBtn').attr('href',$J(this).val());
                    $J('.bottomMoveBtn').attr('target','_blank');
                } else {
                    $J('.bottomMoveBtn').attr('href','');
                    $J('.bottomMoveBtn').attr('target','_self');
                }
            }
        });
    
    
    
    // �뺣�異뺤냼踰꾪듉 ***************************************	
    function $zoom(){
        var nowZoom = 100;
        var size=document.getElementById("size");			
    
        $J(".zoomIn").click(function(){
            zoom_in();
        });
        $J(".zoomOut").click(function(){
            zoom_out();
        });
        $J(".zoomOrg").click(function(){
            zoom_org();
        });
        function $zoom(){
            document.body.style.zoom=nowZoom+"%";
        }
        function zoom_out(){
            nowZoom-=10;
            if(nowZoom<70){
                alert("�붿씠�� 異뺤냼�� �� �놁뒿�덈떎.");
                nowZoom=70;
            }	
            $zoom();				
            size.innerHTML=nowZoom+"%";				
        } 
        function zoom_in(){
            nowZoom+=10;				
            if(nowZoom>150){
                alert("�붿씠�� �뺣��� �� �놁뒿�덈떎.");
                nowZoom=150;
            }
            $zoom();
            size.innerHTML=nowZoom+"%";
        }
        function zoom_org(){
            nowZoom = 100;	
            $zoom();
            size.innerHTML=nowZoom+"%";
        }	
    }
    
    
    // 硫붾돱寃��� ***************************************
    
        
        
    // �� *************************************************	
        // ��1
        // 蹂��� �좎뼵遺��� 理쒖긽�⑥뿉 �꾩튂	
        function tab1ResizeForPc(){	
            if(tab1Li.length && tab1Len > 6){
                tab1Li.css('width', '16.66%');
                for(var i=6; i < 12; i++){
                    tab1Li.eq(i).children().css('border-top',0);
                }
                tab1Li.eq(6).children().css({'border-left':'1px solid #d5d5d5'});
                $J('.tab1 ul').css({'background-position':'right -66px','background-color':'#fff','background-image':'none'});
            }else{
                tab1Li.css('width', 100/tab1Len + '%');
            }	
            if(tab1Li.length){
                $J('.tab1 ul li').each(function(){
                    var tab1SpanPercentage = $J(this).children().children().width() / $J(this).children().width();
                    //console.log(tab1SpanPercentage);
                    if(tab1SpanPercentage > 0.79){
                        //$J(this).children().children().css({'font-size':'16px','line-height':'20px'});
                        $J(this).children().children().css({'line-height':'20px'});
                        //$J('.tab1 ul li a').css({'height':'56px','line-height':'52px'});
                    }else {
                        //$J(this).children().children().css({'font-size':'18px'});
                        //$J('.tab1 ul li a').css({'height':'56px','line-height':'52px'});
                    }
                });
            }
        }
        function tab1ResizeForMobile(){
            if(tab1Li.length && tab1Len > 2){
                $J('.tab1 ul li').css('width', '33.33%');
            }else {
                $J('.tab1 ul li').css('width', 100/tab1Len+'%');
            }
            
            if(tab1Li.length){
                $J('.tab1 ul li').children().css({'border-left':'1px solid #fff','border-bottom':'1px solid #fff','border-top':'0','border-right':'0'});
                $J('.tab1 ul li').children().not('.on').css({'background':'#e0e0e0'});
            }
            if(tab1Li.length){
                $J('.tab1 ul li').each(function(){
                    var tab1SpanPercentage = $J(this).children().children().width() / $J(this).children().width();
                    //console.log(tab1SpanPercentage);
                    if(tab1SpanPercentage > 0.79){
                        //$J(this).children().children().css({'font-size':'16px','line-height':'16px'});
                        $J(this).children().children().css({'line-height':'16px'});
                        $J('.tab1 ul li a').css({'height':'49px','line-height':'44px'});
                    }
                });
            }
        }
        // ��2
        tab2ResizeForPc();
        // 蹂��� �좎뼵遺��� 理쒖긽�⑥뿉 �꾩튂	
        function tab2ResizeForPc(){
            if(tab2Li.length && tab2Len > 6){
                tab2Li.css('width', '16.66%');
                for(var i=6; i < 12; i++){
                    tab2Li.eq(i).children().css('border-top',0);
                }
                tab2Li.eq(6).children().css({'border-left':'1px solid #d5d5d5'});
                $J('.tab2 ul').css({'background-position':'right -66px','background-color':'#fff','background-image':'none'});
            }else{
                tab2Li.css('width', 100/tab2Len + '%');
            }
            if(tab2Li.length){
                $J('.tab2 ul li').each(function(){
                    var tab2SpanPercentage = $J(this).children().children().width() / $J(this).children().width();
                    if(tab2SpanPercentage > 0.8 || $J(this).has('br')){
                        $J(this).children().children().css({'font-size':'16px'});
                        $J('.tab2 ul li a').css({'height':'56px','line-height':'52px'});
                    }
                });
            }
        }
        function tab2ResizeForMobile(){
            $J('.tab2 ul li').css('width', '33.33%');
            if(tab2Li.length){
                $J('.tab2 ul li').each(function(){
                    var tab2SpanPercentage = $J(this).children().children().width() / $J(this).children().width();
                    if(tab2SpanPercentage > 0.8 || $J(this).has('br')){
                        $J(this).children().children().css({'font-size':'16px'});
                        $J('.tab2 ul li a').css({'height':'49px','line-height':'44px'});
                    }
                });
            }
        }
        //��3
        if($J('.tab3 ul li a').length){
            $J('.tab3 ul li a').click(function(){
                var tab3Index = $J(this).parent().index() + 1;
                $J('.tab3Target').hide();
                $J('.tab3Target'+tab3Index).show();
                $J('.tab3 ul li a').removeClass('on');
                $J(this).addClass('on');
            });
        }
        
    // www 諛섏쓳�� �щ씪�대뱶. 媛꾨떒. ******************************	
        if($J('.slider_rs').length){
            var slider_rs_li = $J('.slider_rs li');	
            var slider_rs_idx = 0;	
            var slider_rs_length = slider_rs_li.length;
            slider_rs_init();
            $J('.slider_rs .control_prev').click(slider_rs_go_left);
            $J('.slider_rs .control_next').click(slider_rs_go_right);
        }
        function slider_rs_init(){
            slider_rs_li.hide();
            slider_rs_li.eq(0).show();
        }
        function slider_rs_go_left(){
            if(slider_rs_idx == 0){
                slider_rs_idx = slider_rs_length-1;
            }else {
                slider_rs_idx = slider_rs_idx - 1;
            }	
            slider_rs_li.hide();
            slider_rs_li.eq(slider_rs_idx).show();
        }
        function slider_rs_go_right(){
            if(slider_rs_idx == slider_rs_length-1){
                slider_rs_idx = 0;
            }else {
                slider_rs_idx = slider_rs_idx + 1;
            }	
            slider_rs_li.hide();
            slider_rs_li.eq(slider_rs_idx).show();
        }
    
    // www 諛섏쓳�� �щ씪�대뱶. p28�꾩슜�� �섏꽌�숉깂吏���. ******************************	
        if($J('.slider_rs_red').length){
            var slider_rs_red_li = $J('.slider_rs_red li');	
            var slider_rs_red_idx = 0;	
            var slider_rs_red_length = slider_rs_red_li.length;
            slider_rs_red_init();
            $J('.slider_rs_red .control_prev').click(slider_rs_red_go_left);
            $J('.slider_rs_red .control_next').click(slider_rs_red_go_right);
        }
        function slider_rs_red_init(){
            slider_rs_red_li.hide();
            slider_rs_red_li.eq(0).fadeIn();
        }
        function slider_rs_red_go_left(){
            if(slider_rs_red_idx == 0){
                slider_rs_red_idx = slider_rs_red_length-1;
            }else {
                slider_rs_red_idx = slider_rs_red_idx - 1;
            }	
            slider_rs_red_li.hide();
            slider_rs_red_li.eq(slider_rs_red_idx).fadeIn();
        }
        function slider_rs_red_go_right(){
            if(slider_rs_red_idx == slider_rs_red_length-1){
                slider_rs_red_idx = 0;
            }else {
                slider_rs_red_idx = slider_rs_red_idx + 1;
            }	
            slider_rs_red_li.hide();
            slider_rs_red_li.eq(slider_rs_red_idx).fadeIn();
        }
    
    
    // �꾩슜�� slider (= etk_kr main slider) ***************************************	
        var sl2Li = $J('.slider_wrap2 > .slider > li');
        var sl2Len = sl2Li.length - 1;
        var sl2TimeList = [5000,5000,5000,5000];
        var sl2nowPlay = 0;
        var sl2Num = 0;
        var sl2Timer;
        for(var i = 0; i <= sl2Len; i++){
            $J('.slider_wrap2 .slider_point').append('<a href="javascript:void(0);" class="sl_circle"><img src="/images/btn_slide_li.png" alt="' + (i+1) + '踰덉㎏ �대�吏�" /></a>');
        }
        $J('.slider_wrap2 .left').on('click',function(){
            sl2GoLeft();
            sl2nowPlay = 0;
            sl2playBtnSet();
        });
        $J('.slider_wrap2 .right').on('click',function(){
            sl2GoRight();
            sl2nowPlay = 0;
            sl2playBtnSet();
        });
        $J('.slider_wrap2 .play').on('click',function(){
            sl2Play();
            sl2playBtnSet();
        });
        $J('.slider_wrap2 .hold').on('click',function(){
            sl2Hold();
            sl2nowPlay = 0;
            sl2playBtnSet();
        });
        $J('.slider_wrap2 .sl_circle').on('click',function(){
            sl2Num = $J(this).index();
            sl2Hold();
            sl2nowPlay = 0;
            sl2Run();
        });
        //sl2Play();
        sl2circleBtnSet();
        function sl2GoLeft(){
            if(sl2Num == 0) {
                sl2Num = sl2Len;
            }else {
                sl2Num--;
            }
            sl2Hold();
            sl2Run();
        }
        function sl2GoRight(){
            if(sl2Num == sl2Len) {
                sl2Num = 0;
            }else {
                sl2Num ++;
            }
            sl2Hold();
            sl2Run();		
        }	
        function sl2Play(){
            sl2Timer = setInterval(sl2TimerWrap, 5000); // 濡쒕뱶�� 泥� �쒓컙
            sl2nowPlay = 1;
        }
        function sl2Hold(){
            clearInterval(sl2Timer);
        }
        function sl2Run(){
            sl2Li.hide();
            sl2Li.eq(sl2Num).fadeIn('fast');
            sl2circleBtnSet();
            sl2playBtnSet();
        }	
        function sl2TimerWrap() {
            var sl2TimeList = new Array(5000,5000,5000,5000);		
            sl2GoRight();
            clearInterval(sl2Timer);
            sl2Timer = setInterval(sl2TimerWrap, sl2TimeList[sl2Num]);
        }
        function sl2playBtnSet() {
            if(sl2nowPlay){
                $J('.hold').show();
                $J('.play').hide();
            }else{
                $J('.hold').hide();
                $J('.play').show();
            }
        }
        function sl2circleBtnSet(){
            $J('.slider_wrap2 .sl_circle').each(function(){
                $J(this).children().attr('src','https://etk.srail.kr/images/btn_slide_li.png');
            }).eq(sl2Num).children().attr('src','https://etk.srail.kr/images/btn_slide_now.png');
        }
    
    // etk �뱀감沅뚯삁�쏀럹�댁� ******************************	
        // �댁텧諛쒖� 紐⑹쟻吏� �ㅼ쐞移�
        $J.fn.swap = function (elem) {
            elem = elem.jquery ? elem : $J(elem);
            return this.each(function () {$J(document.createTextNode('')).insertBefore(this).before(elem.before(this)).remove();});		
        };
        $J('#btnStationSwitch').click(function () {$J('.station_s').swap('.station_e');});
        // �댄븷�몄듅李④텒 �좎씤援щ텇
    
        
        
        
    // 怨듯넻 - view�섏씠吏� �뚯씠釉� th �믪씠 議곗젅 ******************************	
        /*
        viewTrHeight();
        function viewTrHeight(){
            if($J('.view_tr').length){
                $J('.view_tr').each(function(){
                    var viewTrH = $J(this).height();
                    //$J(this).children('.l').height('auto');
                    //$J(this).children('.r').height('auto');				
                    if(WinSize > mobilePoint){
                        $J(this).children().height(viewTrH-30);
                    }else{
                        $J(this).children().height(viewTrH-20);
                    }
                });
            }
        }
        */
        
        
    // �쇰툝 �쒖뿰�� - 二쇱냼 �놁쑝硫� �뚯깋泥섎━ ******************************		
        /*
        $J('.gnb a').each(function(){
            if($J(this).attr('href') === '' || $J(this).attr('javascript:void(0);')){
                $J(this).css('color','#cecece');
            }
        });
        */
        
        
    // 濡쒕뵫諛�
        $J('.cover-spin').click(function(){
            $J('#cover-spin').show(0);
        });
    
    // S01 寃��됰컯�� - ���됲듃諛뺤뒪 2媛쒖씪�� input 湲몄씠媛� �덈Т �묐떎(諛섏쓳��) -> 洹몃옒�� �쒖뭏 �대┛��.
        function srchWrap2InputSize(){
            if($J('.sub_srch_wrap2').children('div').length >= 2){
                if(isMobile){
                    $J('.sub_srch_wrap2 input').css({'width':'calc(100% - 73px)','margin-top':'5px'});
                    $J('.sub_srch_wrap2 button').css({'margin-top':'5px'});
                }else{
                    $J('.sub_srch_wrap2 input').css({'width':'calc(100% - 285px)','margin-top':'0'});
                    $J('.sub_srch_wrap2 button').css({'margin-top':'0'});
                }
            }
            /*if(isMobile && $J('.sub_srch_wrap2' && $J('.sub_srch_wrap2').children('div').length == 2)){
                $J('.sub_srch_wrap2 input').css({'width':'calc(100% - 73px)','margin-top':'5px'});
                $J('.sub_srch_wrap2 button').css({'margin-top':'5px'});
            }*/
        }
        
    // �명꽣 硫붾돱 泥ル쾲吏몄옄�� �됯퉼蹂�寃�
        $J('.f_li_wrap li').each(function(){
            if($J(this).find('a').text() == '媛쒖씤�뺣낫泥섎━諛⑹묠'){
                if($J('.footer-e').length){
                    //$J(this).find('a').css('color','#fff900'); �묎렐�깆옉��
                    $J(this).find('a').css({'color':'#0000C0','font-weight':'bold', 'font-size': 'large'});
                }else{
                    $J(this).find('a').css('color','#ff9000');				
                }
            }
        });
    
    
    // www > main > �쏀넗洹몃옩3媛쒕찓��
        if($J('.quick_wrap').length){
            var quick_wrap_height = 0;
            $J('.container-w .quick_wrap_box a').each(function(){
                if($J(this).height() > quick_wrap_height){
                    quick_wrap_height = $J(this).height();
                    
                }
                console.log(quick_wrap_height);
            });
            $J('.container-w .quick_wrap_box a').css('height',quick_wrap_height);		
        }
        
    // �뱁몴以��묒뾽. view�먯꽌 p瑜� div濡� �꾪솚 �� �곷떒 �대�吏� 媛��대뜲 �뺣젹.
        if($J('.view_wrap').length){
            $J('.view_wrap td > div > img').parent().css('text-align','center');
        }
    
    // �묎렐�깆옉��
        $J('a[href="#container"]').click(function(){
            //var cansee = $J($J(this).attr('href')).offset().top - 20;
            //$J('html, body').animate( { scrollTop : cansee }, 20 );
            $J('html, body').animate( { scrollTop : 0 }, 20 );
        });
        $J('#container').focus(function(){
            $J('html, body').animate( { scrollTop : 0 }, 20 );
        });
        $J('.best_more').focus(function(){
            $J('html, body').animate( { scrollTop : 900 }, 20 );
        });
        $J('.skip_nav > a').eq(0).click(function(){
            $J('#gnb').focus();
        });
        $J('.skip_nav > a').eq(1).click(function(){
            $J('#container').focus();
        });
    
        
    });
    
        