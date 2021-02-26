
#! -*- coding:utf-8 -*-
import os

from flask_migrate import MigrateCommand
from flask_script import Manager, Server

from App.models.admin import Admin
from App.models.user import User
from App import create_app

app = create_app()
# env=os.environ.get("")
manager=Manager(app)
manager.add_command('db',MigrateCommand)
# manager.add_command("runserver", Server())
if __name__ == '__main__':
    manager.run()