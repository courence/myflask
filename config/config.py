#encoding:utf-8
'''

Created on Jul 7, 2016
@author: jh
'''
import os

# configuration
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = os.path.join(ROOT,'database','myflask.db')
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'



if __name__ == '__main__':
    pass