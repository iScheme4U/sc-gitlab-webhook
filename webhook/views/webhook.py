"""The WebHook service

Copyright (c) 2021 Scott Lau
"""
import logging

from flask import request

from webhook import server


@server.route('/webhook')
def webhook():
    logging.debug(request.json)
    return 'OK'
