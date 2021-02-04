# The MIT License (MIT)
#
# Copyright (c) 2021 Scott Lau
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import unittest

from webhook.handlers import LoggingHandler, MessageQueueHandler, NoOpHandler, ValidateHandler
from webhook.utils import log_init


class HandlerTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        log_init()

    def test_handlers(self):
        json = "json test"
        noop_handler = NoOpHandler()
        logging.getLogger(__name__).info('noop handle')
        result = noop_handler.handle(json)
        self.assertTrue(result)
        handler = LoggingHandler()
        logging.getLogger(__name__).info('login handle None')
        result = handler.handle(None)
        self.assertTrue(result)
        logging.getLogger(__name__).info('login handle json')
        result = handler.handle(json)
        self.assertTrue(result)
        validate_handler = ValidateHandler()
        handler = LoggingHandler(validate_handler)
        logging.getLogger(__name__).info('login and validate handler handle json')
        result = handler.handle(json)
        self.assertTrue(result)
        result = handler.handle(None)
        self.assertFalse(result)

    def test_message_queue_handler(self):
        json = "json test"
        validate_handler = ValidateHandler()
        logging_handler = LoggingHandler(validate_handler)
        handler = MessageQueueHandler(logging_handler)
        logging.getLogger(__name__).info('message queue login and validate handler handle json')
        result = handler.handle(json)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
