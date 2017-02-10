/**
 * ajax相关操作
 */
var HAjax = {
	/**原始ajax请求*/
	ajax : function(type,url,contentType,data, success, error,dataType) {
		if(success==undefined)success=HAjax.success;
		if(error==undefined)error=HAjax.error;
		$.ajax({
					type : type,
					url : url,
					contentType : contentType,//"application/json; charset=utf-8",
					data : data,
					success : success,
					error : error,
					dataType : dataType//"json"
				});
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
	jsonPost : function(url, data, success, error) {
		HAjax.ajax("post",url,"application/json; charset=utf-8",data, success, error,"json");
	},
	/** json get */
	jsonGet : function(url, data, success, error) {
		HAjax.ajax("get",url,"application/json; charset=utf-8",data, success, error,"json");
	},
	/** json get */
	jsonPut : function(url, data, success, error) {
		HAjax.ajax("put",url,"application/json; charset=utf-8",data, success, error,"json");
	}
}