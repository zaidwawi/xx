#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask import (
    Flask,
    request,
    abort,
    jsonify
    )
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db
def create_app(test_config=None):

    # create and configure the app

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def home():
        return 'zaid-wawi'

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run()
