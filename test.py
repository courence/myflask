#encoding:utf-8
'''

Created on Feb 18, 2016
@author: jh
'''



from contextlib import closing
import datetime
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import os
import sqlite3


# configuration
ROOT = os.path.dirname(os.path.abspath(__file__))

DATABASE = os.path.join(ROOT,'database','myflask.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('database/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
        
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    g.db.close()
    
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, content from diary order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    now = datetime.datetime.now()
    snow = now.strftime("%Y-%m-%d %H:%M:%S")
    sdate = now.strftime("%Y-%m-%d")
    type_code = 'personal'
    g.db.execute('insert into diary (date,type_code,title, content,updated_at,created_at) values (?,?,?,?,?,?)',
                 [sdate,type_code,request.form['title'], request.form['text'],snow,snow])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


    
if __name__ == '__main__':
#     app.run()
    init_db()