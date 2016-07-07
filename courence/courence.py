#encoding:utf-8
'''

Created on Jul 7, 2016
@author: jh
'''

from flask import Blueprint,render_template,g,redirect, url_for,request
import datetime

courenceBlueprint = Blueprint('courence', __name__,
                        template_folder='templates')


@courenceBlueprint.route('/courence/index')
def show_entries():
    cur = g.db.execute('select created_at, content from courence order by created_at desc limit 10')
    entries = [dict(created_at=row[0], content=row[1]) for row in cur.fetchall()]
    entries.reverse()
    return render_template('courence/index.html', entries=entries)

@courenceBlueprint.route('/courence/add', methods=['POST'])
def add_entry():
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    g.db.execute('insert into courence (date, content,user_id,updated_at,created_at) values (?,?,?,?,?)',
                 [sdate, request.form['content'],1,snow,snow])
    g.db.commit()
    return redirect(url_for('courence.show_entries'))

if __name__ == '__main__':
    pass
