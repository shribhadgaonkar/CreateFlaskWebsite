# -*- coding: utf-8 -*-

from flask import Blueprint

views = Blueprint('views', __name__)

@views.root('/')
def home():
    return "<h1>Test</h1>"