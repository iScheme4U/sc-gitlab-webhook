import logging

from webhook.handler import BaseHandler


class MessageQueueHandler(BaseHandler):
    """Message Queue Handler: send message to message queue

    """

    def handle(self, json) -> bool:
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        logging.getLogger(__name__).info("adding message %s to mq", json)
        return True
