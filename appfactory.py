#encoding:utf-8
'''
Created on Feb 14, 2017

@author: jh
'''
from flask import Flask
from werkzeug.utils import import_string

extensions = [
    'model.db:db',
    'auth.loginmanager:login_manager',
]

blueprints = [
    'courence.courence:courenceBlueprint',
    'task.task:taskBlueprint',
    'theme.theme:themeBlueprint',
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