"""The WebHook service

Copyright (c) 2021 Scott Lau
"""

from flask import request

from webhook import server
from webhook.handler import LoggingHandler

handler = LoggingHandler()


@server.route('/webhook', methods=['POST'])
def webhook():
    handler.handle(request.json)
    return 'OK'
