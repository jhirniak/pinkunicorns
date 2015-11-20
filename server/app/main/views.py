from flask import request, render_template
from . import main


@main.route("/")
def hello():
    return 'Server is running'


@main.route('extension/', methods=['POST'])
def extension():
    
    import ipdb; ipdb.set_trace()
    return '', 201


@main.route('view/birthday', methods=['POST'])
def view_birthday():

    # display likes

    # display suggested presents with links

    return render_template('birthday.html')


@main.route('view/travel', methods=['POST'])
def view_travel():

    return '', 200


@main.route('view/meeting', methods=['POST'])
def view_meeting():

    return '', 200
