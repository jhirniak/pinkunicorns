from flask import request
from . import main


@main.route("/")
def hello():
    return 'Server is running'


@main.route('extension/', methods=['POST'])
def extension():
    
    import ipdb; ipdb.set_trace()
    return '', 201

