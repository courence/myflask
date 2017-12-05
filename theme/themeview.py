#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request

from common.jsonresult import AjaxResult
from flask_login import current_user, login_required
from model.thememodel import Theme
from model.themecontentmodel import ThemeContent


themeBlueprint = Blueprint('theme', __name__,
                        template_folder='templates')


@themeBlueprint.route('/theme/index')
@login_required
def showLatest():
    return render_template('theme/index.html')

@themeBlueprint.route('/theme/latest',methods=['GET'])
@login_required
def getLatest():
    pagination = Theme.query.filter_by(user_code=current_user.username).order_by(Theme.created_at.desc()).paginate(1, per_page=10)
    return AjaxResult.successResult(pagination.items)

@themeBlueprint.route('/theme/add/index', methods=['GET'])
@login_required
def addIndex():
    return render_template('theme/addindex.html')

@themeBlueprint.route('/theme/add', methods=['POST'])
@login_required
def addDo():
    name = description = request.form['content']
    if name:
        Theme(name,description).save()
    return redirect(url_for('theme.showLatest'))

@themeBlueprint.route('/theme/<int:theme_id>',methods=['get'])
@login_required
def getTheme(theme_id):
    theme = Theme.query.filter_by(user_code=current_user.username,id=theme_id).first()
    return AjaxResult.successResult(theme)


@themeBlueprint.route('/theme/<int:theme_id>/index')
@login_required
def show_content(theme_id):
    theme = Theme.query.filter_by(user_code=current_user.username,id=theme_id).first()
    return render_template('theme/show_content.html',theme=theme)

@themeBlueprint.route('/theme/<int:theme_id>/content')
@login_required
def getcontents(theme_id):
    
    pagination = ThemeContent.query.filter_by(user_code=current_user.username,theme_id=theme_id).order_by(ThemeContent.created_at).paginate(1, per_page=10)
    return AjaxResult.successResult(pagination.items)


@themeBlueprint.route('/theme/<int:theme_id>/add', methods=['POST'])
@login_required
def add_content(theme_id):
    content = request.form['content']
    if content:
        ThemeContent(theme_id,content).save()
    return redirect(url_for('theme.show_content',theme_id=theme_id))



if __name__ == '__main__':
    pass
