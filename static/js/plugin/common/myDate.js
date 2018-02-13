/**
 * 时间选择控件
 */

document.write("<script language=javascript src='" + GParam.staticDomain + "/js/plugin/My97DatePicker/WdatePicker.js'></script>");

var HSelectDate = {
	/**绑定时间控件*/
	bindDate: function (obj, pattern) {
		obj.addClass("Wdate");
		obj.bind('focus', { pattern: pattern }, function (event) {
			var pattern = event.data.pattern || "yyyy-MM-dd";
			WdatePicker({ dateFmt: pattern });
			$(this).blur();
		});
	},
	clickDate: function (proxy, obj, pattern) {
		obj.addClass("Wdate");
		proxy.bind('click', { pattern: pattern, obj: obj }, function (event) {
			HSelectDate.bindDate(obj, event.data.pattern)
			event.data.obj.focus();
		});
	}
}

