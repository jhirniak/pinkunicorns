from flask import request

from . import main

@main.route("/")
def hello():
    return 'Server is running'
