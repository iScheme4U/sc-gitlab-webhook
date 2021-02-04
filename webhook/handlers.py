#  The MIT License (MIT)
#
#  Copyright (c) 2021. Scott Lau
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
import logging

from webhook.producer import ScProducer


class Handler(object):
    """The root handler"""

    def handle(self, json):
        return True


class BaseHandler(Handler):
    """Base handler for decorating use"""

    _handler: Handler = None

    def __init__(self, handler: Handler = None) -> None:
        self._handler = handler

    @property
    def handler(self):
        return self._handler

    def handle(self, json):
        if self._handler:
            return self._handler.handle(json)
        return True


class LoggingHandler(BaseHandler):
    """Logging handler: logging request json to file

    """

    def handle(self, json):
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        logging.getLogger(__name__).info("request json: %s", json)
        return True


class MessageQueueHandler(BaseHandler):
    """Message Queue Handler: send message to message queue

    """

    _producer: ScProducer = None

    def __init__(self, handler: Handler = None) -> None:
        BaseHandler.__init__(self, handler)
        self._producer = ScProducer()

    def handle(self, json) -> bool:
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        return self._producer.send_msg(msg_body=json)


class NoOpHandler(Handler):
    """No Operation handler

    """

    def handle(self, json):
        return True


class ValidateHandler(BaseHandler):
    """Validate json before handling

    """

    def handle(self, json):
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        if not json:
            logging.getLogger(__name__).info("no request json")
            return False
        return True
