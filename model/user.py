#encoding:utf-8
'''
Created on Feb 14, 2017

@author: jh
'''
import datetime
from flask.ext.login import UserMixin

from db import db
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(128), unique=True)
    is_actice = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self, username=None, password=None,email=None,phone=None):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.is_actice = True
        now = datetime.datetime.now()
        snow = now.strftime("%Y-%m-%d %H:%M:%S")
        self.created_at = snow
        self.updated_at = snow
        
    def is_authenticated(self):
            return True

    def is_actice(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<User %r>' % self.username