#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
import datetime
from flask import Blueprint, render_template, g, redirect, url_for, request, jsonify

from common.jsonresult import AjaxResult


taskBlueprint = Blueprint('task', __name__,
                        template_folder='templates')


@taskBlueprint.route('/task/newtasks/index',methods=['GET'])
def showNewTasks():
    '''显示待完成的任务页面'''
    return render_template('task/index.html')

@taskBlueprint.route('/task/newtasks',methods=['GET'])
def getNewTasks():
    '''获取待完成任务'''
    sql = '''
    SELECT priority,content,id,state  from task 
    where type='daily' or state = 'new'
    ORDER BY priority
    '''
    cur = g.db.execute(sql)
    entries = [dict(priority=row[0],content=row[1],id=row[2],state=row[3]) for row in cur.fetchall()]
    return AjaxResult.successResult(entries)

@taskBlueprint.route('/task/newtasks/<int:taskId>/finish',methods=['PUT'])
def finish(taskId):
    '''任务改为完成状态'''
    now = datetime.datetime.now()
    nowstr = now.strftime("%Y-%m-%d %H:%M:%S")
    sql = '''
    update task set state = 'finish',updated_at=? where id=? 
    '''
    g.db.execute(sql,[nowstr,taskId])
    g.db.commit()
    return AjaxResult.successResult()


@taskBlueprint.route('/task/add/index', methods=['GET'])
def addindex():
    '''添加任务页面'''
    now = datetime.datetime.now()
    begin_date = now.strftime("%Y-%m-%d")
    end_date = begin_date
    return render_template('task/addindex.html',begin_date=begin_date,end_date=end_date)

@taskBlueprint.route('/task/add/do', methods=['POST'])
def adddo():
    '''添加任务'''
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    begin_date  = request.form['begin_date']
    end_date  = request.form['end_date']
    mtype  = request.form['type']
    priority = request.form['priority']
    state = 'new'#new,ongoing,complete,unfinished
    content = request.form['content']
    sql = """
        insert into task (type, priority,state,begin_date,
        end_date,content,user_id,updated_at,created_at)
        values (?,?,?,?,?,?,?,?,?)
    """
    params = [mtype,priority,state,begin_date,end_date,content,1,snow,snow]
    g.db.execute(sql,params)
    g.db.commit()
    return redirect(url_for('task.showNewTasks'))

if __name__ == '__main__':
    pass

