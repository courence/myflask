#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
import datetime, os
from flask import Blueprint, render_template, g, redirect, url_for, request
from flask_login import current_user, login_required
from common.jsonresult import AjaxResult, obj2Dict
from model.weimagemodel import WeImage

weBlueprint = Blueprint('we', __name__, template_folder='templates')


@weBlueprint.route('/we/<int:page>', methods=['GET'])
@login_required
def index(page):
    '''显示待完成的任务页面'''
    if page < 1:
        page = 1
    return render_template('we/index.html',page=page)


@weBlueprint.route('/we/<int:page>', methods=['POST'])
@login_required
def getImage(page):
    '''获取最近日志信息'''
    pagination = WeImage.query.filter_by(
        user_code=current_user.username).order_by(
            WeImage.created_at.desc()).paginate(
                page, per_page=12)
    return AjaxResult.successResult({
        'pageInfo': obj2Dict(pagination),
        'items': obj2Dict(pagination.items)
    })
    # return AjaxResult.successResult(pagination.items)


@weBlueprint.route('/we/add/index', methods=['GET'])
@login_required
def addIndex():
    '''添加日志页面'''
    return render_template('we/addindex.html')


@weBlueprint.route('/we/add/do', methods=['POST'])
@login_required
def upload_file():
    image = request.files.get('image')
    content = request.form['content']
    if image and content:
        strtime = datetime.datetime.strftime(datetime.datetime.now(),
                                             "%Y%m%d%H%M%S")
        imgdir = os.path.join("static/data/we/", strtime[0:6])
        if not os.path.exists(imgdir): os.makedirs(imgdir)
        suffix = os.path.splitext(image.filename)[1]
        imgName = strtime + suffix
        path = os.path.join(imgdir, imgName)
        image.save(path)
        WeImage(path, content).save()
        return redirect(url_for('we.index'))

    return AjaxResult.failResult()