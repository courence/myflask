#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from db import db
import datetime
from model.basemethod import BaseMethod
from flask_login import current_user

class Task(db.Model,BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.String(32))#A/B/C/D
    begin_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    sign_date = db.Column(db.Date)
    content = db.Column(db.Text)
    user_code = db.Column(db.String(32))
    remark = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    
    def __init__(self,content=None,begin_date=None,end_date=None,priority="B"):
        self.priority = priority
        self.user_code = current_user.username
        self.begin_date = self.__getDate(begin_date)
        self.end_date = self.__getDate(end_date)
        self.sign_date = self.begin_date
        self.content = content
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now
        
        
    def __getDate(self,date):
        try:
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except:
            return datetime.date.today()