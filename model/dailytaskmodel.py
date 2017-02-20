#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from db import db
import datetime
from model.basemethod import BaseMethod
from flask.ext.login import current_user

class DailyTask(db.Model,BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)
    state = db.Column(db.String(32))#success/fail
    priority = db.Column(db.String(32))#A/B/C/D
    begin_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    content = db.Column(db.Text)
    user_code = db.Column(db.String(32))
    remark = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    
    def __init__(self,task,state='success'):
        self.task_id = task.id
        self.priority = task.priority
        self.user_code = task.user_code
        self.begin_date = task.begin_date
        self.end_date = task.begin_date
        self.content = task.content
        self.created_at = task.created_at
        self.updated_at = task.updated_at
        self.state = state
        
        