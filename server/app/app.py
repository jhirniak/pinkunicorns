from flask import Flask
from flask import Blueprint, render_template, abort
from flask.ext.restful import Api

from extensions import bootstrap, db
from settings.config import config

from social.apps.flask_app.default.models import init_social


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
    init_social(app, db)


@app.before_request
def global_user():
    g.user = login.current_user


@login_manager.user_loader
def load_user(userid):
    try:
        return User.query.get(int(userid))
    except (TypeError, ValueError):
        pass


# Make current user available on templates
@app.context_processor
def inject_user():
    try:
        return {'user': g.user}
    except AttributeError:
        return {'user': None}
