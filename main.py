#encoding:utf-8
'''

Created on Feb 18, 2016
@author: jh
'''



from contextlib import closing
from flask import Flask, g, render_template
import sqlite3

from courence.courence import courenceBlueprint
from task.task import taskBlueprint,getTasks
from theme.theme import themeBlueprint


# create our little application :)
app = Flask(__name__)
app.config.from_object('config.config')
app.register_blueprint(courenceBlueprint)
app.register_blueprint(taskBlueprint)
app.register_blueprint(themeBlueprint)


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
def home():
    tasks = getTasks()
    return render_template('index.html',tasks=tasks)



    
if __name__ == '__main__':
    app.run()
#     init_db()