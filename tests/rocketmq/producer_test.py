import logging
import unittest

from rocketmq.client import Producer, Message

from webhook.utils import log_init


class ProducerTestCase(unittest.TestCase):

    @staticmethod
    def setUpClass() -> None:
        log_init()

    def test_produce(self):
        producer = Producer('PID-XXX')
        producer.set_name_server_address('172.16.188.2:9876')
        producer.start()

        msg = Message('YOUR-TOPIC')
        msg.set_keys('XXX')
        msg.set_tags('XXX')
        msg.set_body('XXXX')
        ret = producer.send_sync(msg)
        logging.info("msg send: %s, %s, %s", ret.status, ret.msg_id, ret.offset)
        producer.shutdown()


if __name__ == '__main__':
    unittest.main()
