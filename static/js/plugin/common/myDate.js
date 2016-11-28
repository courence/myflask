/**
 * 时间选择控件
 */

document.write("<script language=javascript src='"+GParam.staticDomain+"/js/plugin/My97DatePicker/WdatePicker.js'></script>");

var HSelectDate = {
		/**绑定时间控件*/
		bindDate:function(obj,pattern){
			obj.addClass("Wdate");
			obj.bind('focus', function() {
				var pattern = pattern||"yyyy-MM-dd";
				WdatePicker({dateFmt:pattern});
				$(this).blur();
			}); 
		}
}

