"""Hello Service

Copyright (c) 2021 Scott Lau
"""
from webhook import server


@server.route('/hello')
def hello():
    return 'Hello, World'
