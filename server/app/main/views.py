from flask import render_template
from . import main


@main.route("/")
def hello():
    return 'Server is running'


@main.route("frame/")
def frame():
    return render_template('frame.html')

