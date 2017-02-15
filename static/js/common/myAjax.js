/**
 * ajax相关操作
 */
var HAjax = {
	/**原始ajax请求
	 * {
	 * 	type : get,post,put,delete,
	 * 	url : url,
	 *  contentType : 'application/x-www-form-urlencoded',application/json; charset=utf-8
	 *  data:{},
	 *  success:function,
	 *  error:function,
	 *  dataType:"json"
	 * }
	 * */
	ajax : function(param) {
		if(param.success==undefined)param.success=HAjax.success;
		if(param.error==undefined)param.error=HAjax.error;
		$.ajax(param);
	},
	/**默认调用成功行为*/
	success : function(data, textStatus) {
		console.info('调用成功。data:'+JSON.stringify(data)+";textStatus:"+textStatus);
	},
	/**默认调用失败行为*/
	error : function(XMLHttpRequest, textStatus, errorThrown) {
		console.error('调用失败。XMLHttpRequest：'+XMLHttpRequest+';textStatus:'+textStatus+";errorThrown:"+errorThrown);
	},
	/** json post */
	jsonPost : function(param) {
		param.type = "post";
		param.dataType = "json"
		HAjax.ajax(param);
	},
	/** json get */
	jsonGet : function(param) {
		param.type = "get";
		param.dataType = "json"
		HAjax.ajax(param);
	},
	/** json get */
	jsonPut : function(param) {
		param.type = "put";
		param.dataType = "json"
		HAjax.ajax(param);
	}
}