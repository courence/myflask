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
    return render_template('task/index.html', entries=entries)

@taskBlueprint.route('/task/add', methods=['POST'])
def add():
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    mtype = 'once'#once/daily
    priority = 'A'#ABCD
    state = 'new'#new,ongoing,complete,unfinished
    content = request.form['content']
    sql = """
        insert into task (type, priority,state,begin_date,
        end_date,content,user_id,updated_at,created_at)
        values (?,?,?,?,?,?,?,?,?)
    """
    params = [mtype,priority,state,sdate,sdate,content,1,snow,snow]
    g.db.execute(sql,params)
    g.db.commit()
    return redirect(url_for('task.show'))

if __name__ == '__main__':
    pass

