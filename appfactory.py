#encoding:utf-8
'''
Created on Feb 14, 2017

@author: jh
'''
from flask import Flask
import os
from werkzeug.utils import import_string


ROOT = os.path.dirname(os.path.abspath(__file__))
os.sys.path.append(ROOT)

extensions = [
    'model.db:db',
    'auth.loginmanager:login_manager',
]

blueprints = [
    'courence.courenceview:courenceBlueprint',
    'task.taskview:taskBlueprint',
    'theme.themeview:themeBlueprint',
    'auth.auth:ahthBlueprint',
]


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.config')
    for ext_name in extensions:
        ext = import_string(ext_name)
        ext.init_app(app)
    for bp_name in blueprints:
        bp = import_string(bp_name)
        app.register_blueprint(bp)
    return app