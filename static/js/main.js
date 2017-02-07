
$(document).ready(function(){
	$('.nav').find('a').on('click', function() {
		var mainMenuName = $(this).html()
		$.cookie('mainMenuName', mainMenuName, { path: '/' });
	});
	
	//显示当前菜单
	function setActiveMenu(){
		var mainMenuName = $.cookie('mainMenuName');
		if(mainMenuName==null){
			
		}
		else{
			$(".nav a").each(function(){
			    if($(this).html()==mainMenuName){
			    	$(this).parent('.page-scroll').addClass('active')
			    }
			  });
		}
		
	}
	setActiveMenu();
			
});	    	

