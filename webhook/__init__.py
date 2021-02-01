"""sc-gitlab-webhook - The main module

Copyright (c) 2021 Scott Lau
"""
from flask import Flask

__version__ = "0.0.1"

# flask
server = Flask(__name__)

from webhook import views
