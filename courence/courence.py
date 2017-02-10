#encoding:utf-8
'''

Created on Jul 7, 2016
@author: jh
'''

import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request

from common.jsonresult import AjaxResult


courenceBlueprint = Blueprint('courence', __name__,
                        template_folder='templates')

#################################################################

@courenceBlueprint.route('/courence/latest/index')
def showLatest():
    '''显示最近日志信息页面'''
    return render_template('courence/latestindex.html')

@courenceBlueprint.route('/courence/latest',methods=['GET'])
def getLatest():
    '''获取最近日志信息'''
    cur = g.db.execute('select created_at, content from courence order by created_at desc limit 10')
    entries = [dict(createdAt=row[0], content=row[1]) for row in cur.fetchall()]
    return AjaxResult.successResult(entries)


#############################################################

@courenceBlueprint.route('/courence/add/index', methods=['GET'])
def addIndex():
    '''添加日志页面'''
    return render_template('courence/addindex.html')

@courenceBlueprint.route('/courence/add/do', methods=['POST'])
def addDo():
    '''添加日志'''
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    g.db.execute('insert into courence (date, content,user_id,updated_at,created_at) values (?,?,?,?,?)',
                 [sdate, request.form['content'],1,snow,snow])
    g.db.commit()
    return redirect(url_for('courence.showLatest'))

#############################################33333

if __name__ == '__main__':
    pass
