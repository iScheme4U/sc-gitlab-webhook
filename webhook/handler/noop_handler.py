from webhook.handler import Handler


class NoOpHandler(Handler):

    def handle(self, json):
        pass
