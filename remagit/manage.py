# -*- coding: utf-8 -*-
__author__ = 'wangting'

import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG' or 'default'))
