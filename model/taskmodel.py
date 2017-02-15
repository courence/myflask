#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from db import db
import datetime
from model.basemethod import BaseMethod
from flask.ext.login import current_user

class Task(db.Model,BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))#once/daily
    priority = db.Column(db.String(32))#A/B/C/D
    state = db.Column(db.String(32))#new/finish
    begin_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    content = db.Column(db.Text)
    user_code = db.Column(db.String(32))
    remark = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    
    def __init__(self,content=None,begin_date=None,end_date=None,mtype="once",priority="B"):
        self.type = mtype
        self.priority = priority
        self.state = 'new'
        self.user_code = current_user.username
        self.begin_date = self.__getDate(begin_date)
        self.end_date = self.__getDate(end_date)
        self.content = content
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now
        
        
    def __getDate(self,date):
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except:
            return datetime.date.today()