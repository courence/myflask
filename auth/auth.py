#encoding:utf-8
'''
Created on Feb 13, 2017

@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request

from common.jsonresult import AjaxResult
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from model.usermodel import User

ahthBlueprint = Blueprint('auth', __name__, template_folder='templates')


@ahthBlueprint.route('/auth/signin', methods=['GET'])
def signin():
    return render_template('auth/signin.html')


@ahthBlueprint.route('/auth/signin', methods=['POST'])
def validAndLogin():
    username = request.values.get('username')
    password = request.values.get('password')
    if password and username:
        user = User.query.filter_by(username=username).first()
        if user and user.validPassword(password) and login_user(
                user, duration=datetime.timedelta(minutes=5)):
            return AjaxResult.successResult()
    return AjaxResult.failResult('登录名或密码错误')


@ahthBlueprint.route('/auth/signup', methods=['GET'])
def signup():
    return render_template('auth/signup.html')


@ahthBlueprint.route('/auth/signup', methods=['POST'])
def register():
    '''注册'''

    username = request.values.get('username')
    email = request.values.get('email')
    password = request.values.get('password')

    if username and User.query.filter_by(username=username).first():
        return AjaxResult.failResult('该用户名已被使用')
    if email and User.query.filter_by(email=email).first():
        return AjaxResult.failResult('该用邮箱已被使用')

    user = User(username, password, email)
    user.save()
    if login_user(user):
        return AjaxResult.successResult()
    else:
        return AjaxResult.failResult()


@ahthBlueprint.route('/auth/signout', methods=['GET'])
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))
