#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request
from flask_login import current_user,login_required
from common.jsonresult import AjaxResult
from model.taskmodel import Task
from model.dailytaskmodel import DailyTask


taskBlueprint = Blueprint('task', __name__,
                        template_folder='templates')


@taskBlueprint.route('/task/newtasks/index',methods=['GET'])
@login_required
def showNewTasks():
    '''显示待完成的任务页面'''
    return render_template('task/index.html')

@taskBlueprint.route('/task/newtasks',methods=['GET'])
@login_required
def getNewTasks():
    '''获取待完成任务'''
    username = current_user.username
    today = datetime.date.today()
    tasks = Task.query.filter(Task.user_code==username,Task.sign_date <= today).order_by(Task.priority,Task.id).all()
    return AjaxResult.successResult(tasks)

@taskBlueprint.route('/task/newtasks/<int:taskId>/success',methods=['PUT'])
@login_required
def signSuccess(taskId):
    '''任务标记'''
    return sign(taskId,state='success')

@taskBlueprint.route('/task/newtasks/<int:taskId>/fail',methods=['PUT'])
@login_required
def signFail(taskId):
    '''任务标记'''
    return sign(taskId,state='fail')

def sign(taskId,state='success'):
    '''任务标记'''
    task = Task.query.filter_by(user_code=current_user.username,id=taskId).first()
    if task:
        now = datetime.datetime.now()
        
        task.updated_at = now  
        if now.date() < task.end_date:
            task.sign_date = (now+datetime.timedelta(days=1)).date()
        else:
            task.sign_date = None
        task.save()
        DailyTask(task,state).save()
        return AjaxResult.successResult()
    else:
        return AjaxResult.failResult("未获取到相关任务")

@taskBlueprint.route('/task/add/index', methods=['GET'])
@login_required
def addindex():
    '''添加任务页面'''
    now = datetime.datetime.now()
    begin_date = now.strftime("%Y-%m-%d")
    end_date = begin_date
    return render_template('task/addindex.html',begin_date=begin_date,end_date=end_date)

@taskBlueprint.route('/task/add/do', methods=['POST'])
@login_required
def adddo():
    '''添加任务'''
    begin_date  = request.form['begin_date']
    end_date  = request.form['end_date']
    priority = request.form['priority']
    content = request.form['content']

    task = Task(content,begin_date,end_date,priority)
    task.save()
    return redirect(url_for('task.showNewTasks'))

if __name__ == '__main__':
    pass

