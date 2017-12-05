#encoding:utf-8
'''
Created on Feb 14, 2017

@author: jh
'''
import datetime,hashlib
from flask_login import UserMixin
from model.basemethod import BaseMethod

from db import db
class User(db.Model,UserMixin,BaseMethod):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(128), unique=True)
    is_active = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, username=None, password=None,email=None,phone=None):
        super(User, self).__init__()
        self.username = username
        self.name = username
        self.password = md5(password)
        self.email = email
        self.phone = phone
        self.is_active = True
        now = datetime.datetime.now()
        self.created_at = now
        self.updated_at = now
    
    def validPassword(self,password):
        return self.password==md5(password)
    

    def __repr__(self):
        return '<User %r>' % self.username
    
def md5(src):

    md5 = hashlib.md5()
    md5.update(src)
    return md5.hexdigest()
    