import unittest

from webhook.handler import LoggingHandler, NoOpHandler
from webhook.utils import log_init


class MyTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        log_init()

    def test_handler(self):
        json = "json test"
        noop_handler = NoOpHandler()
        noop_handler.handle(json)
        handler = LoggingHandler(noop_handler)
        handler.handle(json)
        handler = LoggingHandler()
        handler.handle(json)


if __name__ == '__main__':
    unittest.main()
