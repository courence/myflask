#encoding:utf-8
'''

Created on Feb 18, 2016
@author: jh
'''
from flask_login import login_required, current_user

from flask import render_template

from appfactory import create_app
import datetime

app = create_app()


@app.route('/')
@login_required
def home():
    now = datetime.datetime.now()
    begin = datetime.datetime.strptime("20160725210504", "%Y%m%d%H%M%S")
    end = datetime.datetime.strptime("20491231232359", "%Y%m%d%H%M%S")
    total = (end - begin).days
    used = (now - begin).days
    msg = "%.1f%%  (%d/%d)" % (used * 100.0 / total, used, total)
    return render_template('index.html', msg=msg)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
