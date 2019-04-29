import os
import sys

from sayhello import app

if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

SECRET_KEY = os.getenv('SECRET_KEY', 'FLAG{123456}')

dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
SQLALCHEMY_TARCK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
