#encoding:utf-8
'''
json结果返回
Created on Feb 7, 2017

@author: jh
'''
from flask import jsonify
import datetime

class AjaxResult:
    def __init__(self,state=True,data=None,msg=None ,code=None):
        self.state = state
        self.data = obj2Dict(data)
        self.msg = msg
        self.code = code
        
    def getResult(self):
        return jsonify(state=self.state,data=self.data,msg=self.msg,code=self.code)
    @staticmethod
    def successResult(data=None):
        return AjaxResult(True,data).getResult()
    
    @staticmethod
    def failResult(msg=None,code=None):
        return AjaxResult(False,None,msg,code).getResult()
    

    
                
#         return AjaxResult(False,None,msg,code).getResult()
    
def obj2Dict(obj):
    if isinstance(obj, dict):
        return obj
    elif isinstance(obj, (list,tuple)):
        lst = []
        for item in obj:
            lst.append(obj2Dict(item))
        return lst
    elif hasattr(obj, '__dict__'):
        d = {}
        for key,value in obj.__dict__.items():
            tempvalue = None
            if isinstance(value, (str,dict,int,unicode)):
                tempvalue = value
            elif isinstance(value, datetime.datetime):
                tempvalue = value.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(value, datetime.date):
                tempvalue = value.strftime("%Y-%m-%d")
    #         elif isinstance(value, object):
    #             tempvalue = obj2Dict(value)
            if tempvalue:
                d[key] = tempvalue
        return d
    else:
        return None
                
if __name__ == '__main__':
    print AjaxResult.successResult({'test':1})
    print AjaxResult.failResult("error",'001')