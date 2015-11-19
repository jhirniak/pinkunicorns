from flask import Flask
from settings.config import config
from .extensions import db, bootstrap
from flask.ext.restful import Api

def create_app(config_name):
    """Create a flask app from a config"""
    from .main import resources
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)

    api_url = '/api/v1'

    api = Api(app)
    api.add_resource(resources.PopularShows, api_url + '/popular')

    return app

def register_extensions(app):
    """Register flask extensions"""
    db.init_app(app)
    bootstrap.init_app(app)


