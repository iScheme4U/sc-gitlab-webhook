from webhook.handler import Handler


class NoOpHandler(Handler):
    """No Operation handler

    """

    def handle(self, json):
        return True
