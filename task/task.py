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
    cur = g.db.execute('select updated_at, content from task order by updated_at desc,priority  limit 10')
    entries = [dict(created_at=row[0], content=row[1]) for row in cur.fetchall()]
    entries.reverse()
    now = datetime.datetime.now()
    begin_date = now.strftime("%Y-%m-%d")
    end_date = begin_date
    tasks = get()
    return render_template('task/index.html', entries=entries,tasks=tasks,begin_date=begin_date,end_date=end_date)

def get():
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")
    sql = '''
    SELECT content from task 
    where type='daily' 
    or ( type='once' and begin_date>=? and end_date<=?) 
    ORDER BY priority
    '''
    cur = g.db.execute(sql,[date,date])
    entries = [dict(content=row[0]) for row in cur.fetchall()]
    return entries
#     entries.reverse()

@taskBlueprint.route('/task/add', methods=['POST'])
def add():
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    begin_date  = request.form['begin_date']
    end_date  = request.form['end_date']
    mtype  = request.form['type']
    priority = 'A'#ABCD
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

