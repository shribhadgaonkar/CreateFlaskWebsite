# -*- coding: utf-8 -*-

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "SecreteKeyApp"
    
    return app
