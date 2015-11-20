#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import MigrateCommand

from app.app import create_app




app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
server = Server()
manager.add_command("runserver", server)


def make_shell_context():
    """Populate stuff in flask shell"""
    return dict(app=app, db=db)


# Populate commands
manager.add_command('shell', Shell(make_context=make_shell_context, use_bpython=True))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

