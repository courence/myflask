var CurrentMenuName;
$(document).ready(function () {
	//显示当前菜单
	setActiveMenu();
	//显示登录信息
	showSignInfo();

	//显示登录信息
	function showSignInfo() {
		var url = '/auth/signin';
		var menuName = 'SIGNIN'
		if (window.is_signin) {
			url = '/auth/signout';
			menuName = 'SIGNOUT'
		}
		var html = '<a href="' + url + '">' + menuName + '</a>'
		$(".loginflag").html(html);
	}

	$('.nav').find('a').on('click', function () {
		var mainMenuName = $(this).html()
		$.cookie('mainMenuName', mainMenuName, { path: '/' });
	});

	//显示当前菜单
	function setActiveMenu() {
		var mainMenuName = CurrentMenuName //|| $.cookie('mainMenuName');
		if (mainMenuName == null) {

		}
		else {
			$(".nav a").each(function () {
				if ($(this).html() == mainMenuName) {
					$(this).parent('.page-scroll').addClass('active')
				}
			});
		}

	}


});

