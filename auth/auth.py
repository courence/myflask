#encoding:utf-8
'''
Created on Feb 13, 2017

@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request

from common.jsonresult import AjaxResult
from flask.ext.login import LoginManager, login_required, UserMixin, login_user, logout_user
from model.user import User


ahthBlueprint = Blueprint('auth', __name__,
                        template_folder='templates')


    
@ahthBlueprint.route('/auth/index')
@login_required
def show():
    return render_template('auth/index.html')


@ahthBlueprint.route('/auth/signin', methods=['GET', 'POST'])
def signin():
    admin = User.query.filter_by(username='admin').first()
    print admin
    user = User()
    users = User.query.all()
    
    print users
    print login_user(user)
    return render_template('auth/signin.html')

@ahthBlueprint.route('/auth/signup', methods=['GET'])
def signup():
    
    return render_template('auth/signup.html')

@ahthBlueprint.route('/auth/signup',methods=['POST'])
def register():
    '''注册'''
    
    username = request.values.get('username')
    email = request.values.get('email')
    password = request.values.get('password')
    if not username and User.query.filter_by(username=username).first():
        return AjaxResult.failResult('改用户名已被使用')
    if not email and User.query.filter_by(email=email).first():
        return AjaxResult.failResult('改用邮箱已被使用')
    
    user = User(username,password,email)
    if login_user(user):
        return AjaxResult.successResult()
    else:
        return AjaxResult.failResult()

    


@ahthBlueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return "logout page"    

# test method
@ahthBlueprint.route('/test')
def test():
    return "yes , you are allowed"