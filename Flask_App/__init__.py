from flask import Flask
from flask_bootstrap import Bootstrap
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

exchng_rate_app = Flask(__name__)
exchng_rate_app.config.from_object(Configuration)

bootstrap = Bootstrap(exchng_rate_app)
database = SQLAlchemy(exchng_rate_app)
migration = Migrate(app=exchng_rate_app,db=database)

from Flask_App import routes,models