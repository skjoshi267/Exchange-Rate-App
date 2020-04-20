from flask import Flask
from flask_bootstrap import Bootstrap
from config import Configuration
exchng_rate_app = Flask(__name__)
exchng_rate_app.config.from_object(Configuration)
bootstrap = Bootstrap(exchng_rate_app)
from Flask_App import routes