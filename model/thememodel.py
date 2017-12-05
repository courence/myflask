#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from db import db
import datetime
from model.basemethod import BaseMethod
from flask_login import current_user

class Theme(db.Model,BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    type = db.Column(db.String(32))
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    user_code = db.Column(db.String(32))
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    
    def __init__(self,name,description,mtype='default'):
        self.date = datetime.date.today()
        self.type = mtype
        self.name = name
        self.description = description
        self.user_code = current_user.username
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now