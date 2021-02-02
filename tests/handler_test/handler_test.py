import unittest
import logging

from webhook.handler import LoggingHandler, NoOpHandler, ValidateHandler, MessageQueueHandler
from webhook.utils import log_init


class MyTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        log_init()

    def test_handlers(self):
        json = "json test"
        noop_handler = NoOpHandler()
        logging.info('noop handle')
        result = noop_handler.handle(json)
        self.assertTrue(result)
        handler = LoggingHandler()
        logging.info('login handle None')
        result = handler.handle(None)
        self.assertTrue(result)
        logging.info('login handle json')
        result = handler.handle(json)
        self.assertTrue(result)
        validate_handler = ValidateHandler()
        handler = LoggingHandler(validate_handler)
        logging.info('login and validate handler handle json')
        result = handler.handle(json)
        self.assertTrue(result)
        result = handler.handle(None)
        self.assertFalse(result)

    def test_message_queue_handler(self):
        json = "json test"
        validate_handler = ValidateHandler()
        logging_handler = LoggingHandler(validate_handler)
        handler = MessageQueueHandler(logging_handler)
        logging.info('message queue login and validate handler handle json')
        result = handler.handle(json)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
