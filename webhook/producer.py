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

from rocketmq.client import Producer, Message
from rocketmq.exceptions import RocketMQException

from webhook.exceptions import SendMsgException
from webhook.singleton import Singleton
from webhook.utils import config


class ScProducer(metaclass=Singleton):
    """RocketMQ message producer"""

    _producer: Producer = None
    _topic: str = None
    _keys: str = None
    _tags: str = None

    def __init__(self):
        group_id = config.get("rocketmq.group_id")
        name_server_ip = config.get("rocketmq.name_server_ip")
        port = config.get("rocketmq.name_server_port")
        self._producer = Producer(group_id)
        self._producer.set_name_server_address("{}:{}".format(name_server_ip, port))
        self._topic = config.get("rocketmq.msg_topic")
        self._keys = config.get("rocketmq.msg_keys")
        self._tags = config.get("rocketmq.msg_tags")

    def start(self):
        self._producer.start()

    def shutdown(self):
        self._producer.shutdown()

    def send_msg(self, *, msg_body):
        msg = Message(self._topic)
        msg.set_keys(self._keys)
        msg.set_tags(self._tags)
        msg.set_body(msg_body)
        try:
            ret = self._producer.send_sync(msg)
            logging.getLogger(__name__).info("msg send status: %s, id: %s, offset: %s", ret.status, ret.msg_id,
                                             ret.offset)
            return True
        except RocketMQException as e:
            logging.getLogger(__name__).exception("failed to send message to mq", exc_info=e)
            raise SendMsgException(e)
