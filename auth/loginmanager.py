#encoding:utf-8
'''
Created on Feb 13, 2017

@author: jh
'''
from auth import ahthBlueprint
from model.usermodel import User
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'

    
@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    return user