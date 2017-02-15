#encoding:utf-8
'''
Created on Feb 15, 2017

@author: jh
'''
from model.db import db
class BaseMethod:
    def save(self):
        db.session.add(self)
        db.session.commit()