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

from rocketmq.client import Producer, Message
from scutils import log_init


class ProducerTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        log_init()

    def test_produce(self):
        producer = Producer('PID-XXX')
        producer.set_name_server_address('127.0.0.1:9876')
        producer.start()

        msg = Message('YOUR-TOPIC')
        msg.set_keys('XXX')
        msg.set_tags('XXX')
        msg.set_body('XXXX')
        ret = producer.send_sync(msg)
        logging.getLogger(__name__).info("msg send: %s, %s, %s", ret.status, ret.msg_id, ret.offset)
        producer.shutdown()


if __name__ == '__main__':
    unittest.main()
