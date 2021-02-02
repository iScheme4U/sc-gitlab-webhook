import logging

from webhook.handler.base_handler import BaseHandler


class LoggingHandler(BaseHandler):

    def handle(self, json):
        if not json:
            logging.info("no request json")
            return
        logging.getLogger(__name__).info("request json: %s", json)
        BaseHandler.handle(self, json)
