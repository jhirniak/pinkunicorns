
from flask import Flask

from flask.ext.cors import CORS
from settings.config import config
from .extensions import db, bootstrap

from flask.ext.restful import Api

from extensions import bootstrap, db
from settings.config import config

def create_app(config_name):
    """Create a flask app from a config"""
    from .main import resources
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)

    api_url = '/api/v1'

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    api = Api(app)
    api.add_resource(resources.Analyse, api_url + '/analyse')
    api.add_resource(resources.RunTask, api_url + '/run')
    api.add_resource(resources.GoogleCalendar, api_url + '/gcal')
    api.add_resource(resources.Jarvis, api_url + '/jarvis')

    return app

def register_extensions(app):
    """Register flask extensions"""
    db.init_app(app)
    bootstrap.init_app(app)
    CORS(app)

