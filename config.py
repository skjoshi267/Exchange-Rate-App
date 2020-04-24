import os

class Configuration(object):
    SECRET_KEY = 'Password@123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:admin@localhost/exchange_rate'
    SQLALCHEMY_TRACK_MODIFICATIONS = False