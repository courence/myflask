#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
from flask import Blueprint,render_template,g,redirect, url_for,request
import datetime

taskBlueprint = Blueprint('task', __name__,
                        template_folder='templates')


@taskBlueprint.route('/task/index')
def show():
    now = datetime.datetime.now()
    begin_date = now.strftime("%Y-%m-%d")
    end_date = begin_date
    return render_template('task/index.html', tasks=getTasks(),begin_date=begin_date,end_date=end_date)

def getTasks():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    sql = '''
    SELECT priority,content from task 
    where type='daily' 
    or ( type='once' and begin_date<=? and end_date>=?) 
    ORDER BY priority
    '''
    cur = g.db.execute(sql,[date,date])
    entries = [dict(priority=row[0],content=row[1]) for row in cur.fetchall()]
    return entries
#     entries.reverse()

@taskBlueprint.route('/task/add/index', methods=['GET'])
def addindex():
    now = datetime.datetime.now()
    begin_date = now.strftime("%Y-%m-%d")
    end_date = begin_date
    return render_template('task/addindex.html',begin_date=begin_date,end_date=end_date)

@taskBlueprint.route('/task/add/do', methods=['POST'])
def adddo():
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
    return redirect(url_for('task.show'))

if __name__ == '__main__':
    pass

