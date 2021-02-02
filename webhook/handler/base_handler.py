from webhook.handler.handler import Handler


class BaseHandler(Handler):
    _handler: Handler = None

    def __init__(self, handler: Handler = None) -> None:
        self._handler = handler

    @property
    def handler(self):
        return self._handler

    def handle(self, json):
        if self.handler:
            self._handler.handle(None)
