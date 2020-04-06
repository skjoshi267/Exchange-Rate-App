from flask import Flask
from flask_bootstrap import Bootstrap
exchng_rate_app = Flask(__name__)
bootstrap = Bootstrap(exchng_rate_app)
from Flask_App import routes