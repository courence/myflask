#encoding:utf-8
'''

Created on Feb 18, 2016
@author: jh
'''
from flask_login import login_required

from flask import  render_template

from appfactory import create_app

app = create_app()


    
@app.route('/')
@login_required
def home():
    return render_template('index.html')



    
if __name__ == '__main__':
    app.run()
