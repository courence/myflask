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
    '''show the tasks of today'''
    now = datetime.datetime.now()
    today = datetime.datetime.strftime(now, "%Y-%m-%d")
    username = current_user.username
    tasks = Task.query.filter(Task.user_code == username,
                              Task.date < now.date(), Task.type == "Action",
                              Task.state.in_(["ToDo", "Ongoing"])).all()
    if tasks:
        return render_template('task/undo.html')

    return render_template('task/index.html', today=today)


@taskBlueprint.route('/task/plan', methods=['GET'])
@login_required
def taskPlan():
    '''planing tasks'''
    return render_template('task/plan.html')


@taskBlueprint.route('/task/plans', methods=['GET'])
@login_required
def getplans():
    '''获取待完成任务'''
    username = current_user.username
    date = datetime.date.today()
    tasks = Task.query.filter(Task.user_code == username, Task.type == "Plan",
                              Task.state.in_(["ToDo", "Ongoing"])).order_by(
                                  Task.state, Task.priority, Task.id).all()
    return AjaxResult.successResult({'date': date, 'tasks': obj2Dict(tasks)})


@taskBlueprint.route('/task/<string:date>', methods=['GET'])
@login_required
def getNewTasks(date):
    '''获取待完成任务'''
    username = current_user.username
    try:
        date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except:
        date = datetime.date.today()
    tasks = Task.query.filter(Task.user_code == username, Task.date == date,
                              Task.type == "Action").order_by(
                                  Task.state, Task.priority, Task.id).all()
    return AjaxResult.successResult({'date': date, 'tasks': obj2Dict(tasks)})


@taskBlueprint.route('/task/undo', methods=['GET'])
@login_required
def showUndo():
    '''show unfinished tasks'''
    return render_template('task/undo.html')


@taskBlueprint.route('/task/undo', methods=['POST'])
@login_required
def getUndo():
    '''get unfinished tasks'''
    username = current_user.username
    date = datetime.date.today()
    tasks = Task.query.filter(Task.user_code == username, Task.date < date,
                              Task.type == "Action",
                              Task.state.in_(["ToDo", "Ongoing"])).order_by(
                                  Task.date, Task.priority, Task.id).all()
    return AjaxResult.successResult({'date': date, 'tasks': obj2Dict(tasks)})


@taskBlueprint.route('/task/<int:taskId>/<string:state>', methods=['PUT'])
@login_required
def changestate(taskId, state):
    '''change task state'''
    if state not in ['Ongoing', 'Done', 'Cancel']:
        return AjaxResult.failResult("invalid state:" + state)
    task = Task.query.filter(Task.user_code == current_user.username,
                             Task.id == taskId,
                             Task.state.in_(["ToDo", "Ongoing"])).first()
    if task:
        now = datetime.datetime.now()
        task.updated_at = now
        task.state = state
        task.save()
        if task.type == "Plan" and state in ["ToDo", "Ongoing"]:
            date = now.date()
            if now.hour > 20:
                date = (now + datetime.timedelta(days=1)).date()
            t = Task.query.filter(
                Task.user_code == current_user.username, Task.type == "Action",
                Task.content == task.content, Task.date == date).first()
            if not t:
                t = Task(task.content, date, task.priority, task.created_at)
                t.type = "Action"
                t.save()
        return AjaxResult.successResult()
    else:
        return AjaxResult.failResult("未获取到相关任务")


@taskBlueprint.route('/task/new', methods=['GET'])
@login_required
def addindex():
    now = datetime.datetime.now()
    today = datetime.datetime.strftime(now, "%Y-%m-%d")
    return render_template('task/addindex.html', date=today)


@taskBlueprint.route('/task/new', methods=['POST'])
@login_required
def adddo():
    '''添加任务'''
    date = request.form['date']
    priority = request.form['priority']
    content = request.form['content']
    type = request.form['type']
    if date and priority and content and content.strip() and type in [
            "Plan", "Action"
    ]:
        task = Task(content.strip(), date, priority)
        task.type = type
        task.save()
        return AjaxResult.successResult()
    return AjaxResult.failResult("parameters error")


if __name__ == '__main__':
    pass
