/**
*有效性验证相关操作
*/
var HValid = {
	isEmpty : function(str) {
		return str==undefined || str==null || str=='null' || str=="None";
	},
	isBlank : function(str) {
		return HValid.isEmpty(str) || str=="";
	},
	isEmail : function(str) {
		return str.match(/^(.+)@(.+)\.(.+)$/) != null;
	},
	isPhone : function(str) {
		return str.match(/^1[0-9]{10}$/) != null;
	},
	isUsername : function(str) {
		return str.match(/^[a-zA-Z][0-9a-zA-Z]{1,15}$/) != null;
	},
}