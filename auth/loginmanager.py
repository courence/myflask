#encoding:utf-8
'''
Created on Feb 13, 2017

@author: jh
'''
from auth import ahthBlueprint
from model.user import User
from flask.ext.login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

    
@login_manager.user_loader
def load_user(user_id):
    user = User()
    return user