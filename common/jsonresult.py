#encoding:utf-8
'''
json结果返回
Created on Feb 7, 2017

@author: jh
'''
from flask import jsonify

class AjaxResult:
    def __init__(self,state=True,data=None,msg=None ,code=None):
        self.state = state
        self.data = data
        self.msg = msg
        self.code = code
        
    def getResult(self):
        return jsonify(state=self.state,data=self.data,msg=self.msg,code=self.code)
    @staticmethod
    def successResult(data):
        return AjaxResult(True,data).getResult()
    
    @staticmethod
    def failResult(msg=None,code=None):
        return AjaxResult(False,None,msg,code).getResult()
    
    
if __name__ == '__main__':
    print AjaxResult.successResult({'test':1})
    print AjaxResult.failResult("error",'001')