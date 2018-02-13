#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request
from flask_login import current_user, login_required
from common.jsonresult import AjaxResult, obj2Dict
from model.taskmodel import Task

taskBlueprint = Blueprint('task', __name__, template_folder='templates')


@taskBlueprint.route('/task/newtasks/index', methods=['GET'])
@login_required
def showNewTasks():
    '''显示待完成的任务页面'''
    now = datetime.datetime.now()
    today = datetime.datetime.strftime(now, "%Y-%m-%d")
    return render_template('task/index.html', today=today)


@taskBlueprint.route('/task/<string:date>', methods=['GET'])
@login_required
def getNewTasks(date):
    '''获取待完成任务'''
    username = current_user.username
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except:
        date = datetime.date.today()
    tasks = Task.query.filter(Task.user_code == username,
                              Task.date == date).order_by(
                                  Task.priority, Task.id).all()
    return AjaxResult.successResult({'date': date, 'tasks': obj2Dict(tasks)})


@taskBlueprint.route('/task/<int:taskId>/<string:state>', methods=['PUT'])
@login_required
def changestate(taskId, state):
    '''change task state'''
    if state not in ['Ongoing', 'Done', 'Cancel']:
        return AjaxResult.failResult("invalid state:" + state)
    task = Task.query.filter_by(
        user_code=current_user.username, id=taskId, state="ToDo").first()
    if task:
        now = datetime.datetime.now()
        task.updated_at = now
        task.state = state
        task.save()
        if state == "Ongoing":
            tomorrow = now + datetime.timedelta(days=1)
            Task(task.content, tomorrow.date(), task.priority).save()
        return AjaxResult.successResult()
    else:
        return AjaxResult.failResult("未获取到相关任务")


@taskBlueprint.route('/task/add/index', methods=['GET'])
@login_required
def addindex():
    '''添加任务页面'''
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    return render_template('task/addindex.html', date=date)


@taskBlueprint.route('/task/add/do', methods=['POST'])
@login_required
def adddo():
    '''添加任务'''
    date = request.form['date']
    priority = request.form['priority']
    content = request.form['content']

    task = Task(content, date, priority)
    task.save()
    return redirect(url_for('task.showNewTasks'))


if __name__ == '__main__':
    pass
