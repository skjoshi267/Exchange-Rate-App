class Configuration(object):
    SECRET_KEY = 'Password@123'
    FLASK_ENV = 'development'
    FLASK_APP = 'exchange_rate.py'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/exchange_rate'