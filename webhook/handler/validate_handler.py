import logging

from webhook.handler import BaseHandler


class ValidateHandler(BaseHandler):
    """Validate json before handling

    """

    def handle(self, json):
        result = BaseHandler.handle(self, json)
        if not result:
            return False
        if not json:
            logging.info("no request json")
            return False
        return True
