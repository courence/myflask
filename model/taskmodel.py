#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from db import db
import datetime
from model.basemethod import BaseMethod
from flask_login import current_user


class Task(db.Model, BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    priority = db.Column(db.String(32))  #A/B/C/D
    date = db.Column(db.Date)
    type = db.Column(db.String(32))  #Plan/Action
    state = db.Column(db.String(32))  #ToDo/Ongoing/Done/Cancel
    content = db.Column(db.Text)
    user_code = db.Column(db.String(32))
    remark = db.Column(db.Text)
    updated_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    def __init__(self, content=None, date=None, priority="B", created_at=None):
        self.priority = priority
        self.user_code = current_user.username
        self.date = self.__getDate(date)
        self.state = 'ToDo'
        self.content = content
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now
        if created_at:
            self.created_at = created_at

    def __getDate(self, date):
        try:
            if isinstance(date, datetime.date):
                return date
            return datetime.datetime.strptime(date, "%Y-%m-%d").date()
        except:
            return datetime.date.today()