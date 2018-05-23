#encoding:utf-8
'''

Created on Jul 7, 2016
@author: jh
'''

import datetime
import json
from flask import Blueprint, render_template, g, redirect, url_for, request
from flask_login import current_user, login_required
from common.jsonresult import AjaxResult, obj2Dict
from model.courencemodel import Courence

courenceBlueprint = Blueprint(
    'courence', __name__, template_folder='templates')

#################################################################


@courenceBlueprint.route('/courence/<int:page>', methods=['GET'])
@login_required
def showLatest(page):
    '''显示最近日志信息页面'''
    if page < 1:
        page = 1

    return render_template('courence/index.html', page=page)


@courenceBlueprint.route('/courence/<int:page>', methods=['POST'])
@login_required
def getCourences(page):
    '''获取最近日志信息'''
    pagination = Courence.query.filter_by(
        user_code=current_user.username).order_by(
            Courence.created_at.desc()).paginate(
                page, per_page=10)
    return AjaxResult.successResult({
        'pageInfo': obj2Dict(pagination),
        'items': obj2Dict(pagination.items)
    })


#############################################################


@courenceBlueprint.route('/courence/add/index', methods=['GET'])
@login_required
def addIndex():
    '''添加日志页面'''
    return render_template('courence/addindex.html')


@courenceBlueprint.route('/courence/add/do', methods=['POST'])
@login_required
def addDo():
    '''添加日志'''
    content = request.form['content']
    Courence(content).save()
    return redirect(url_for('courence.showLatest', page=1))


#############################################33333

if __name__ == '__main__':
    pass
