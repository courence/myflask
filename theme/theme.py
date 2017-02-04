#encoding:utf-8
'''

Created on Jul 11, 2016
@author: jh
'''
from flask import Blueprint,render_template,g,redirect, url_for,request
import datetime

themeBlueprint = Blueprint('theme', __name__,
                        template_folder='templates')


@themeBlueprint.route('/theme/index')
def show():
    cur = g.db.execute('select created_at, name,id from theme order by created_at desc limit 10')
    entries = [dict(created_at=row[0], content=row[1],id=row[2]) for row in cur.fetchall()]
    return render_template('theme/index.html', entries=entries)

@themeBlueprint.route('/theme/add/index', methods=['GET'])
def addIndex():
    return render_template('theme/addindex.html')

@themeBlueprint.route('/theme/add/do', methods=['POST'])
def addDo():
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    mtype = 'default'
    name = description = request.form['content']
    sql = """
        insert into theme (date,type,name,description,
        user_id,updated_at,created_at)
        values (?,?,?,?,?,?,?)
    """
    params = [sdate,mtype,name,description,1,snow,snow]
    g.db.execute(sql,params)
    g.db.commit()
    return redirect(url_for('theme.show'))


@themeBlueprint.route('/theme/<int:theme_id>/index')
def show_content(theme_id):
    cur = g.db.execute('select name from theme where id=? ',[theme_id])
    theme = [dict(name=row[0]) for row in cur.fetchall()][0]
    cur = g.db.execute('select created_at, content from theme_content where theme_id=? ',[theme_id])
    entries = [dict(created_at=row[0], content=row[1]) for row in cur.fetchall()]
    return render_template('theme/show_content.html', entries=entries,theme_id=theme_id,theme=theme)

@themeBlueprint.route('/theme/<int:theme_id>/add', methods=['POST'])
def add_content(theme_id):
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    content = request.form['content']
    sql = """
        insert into theme_content (theme_id, date,content,
        user_id,updated_at,created_at)
        values (?,?,?,?,?,?)
    """
    params = [theme_id,sdate,content,1,snow,snow]
    g.db.execute(sql,params)
    g.db.commit()
    return redirect(url_for('theme.show_content',theme_id=theme_id))



if __name__ == '__main__':
    pass
