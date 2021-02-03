import time

from rocketmq.client import PushConsumer, ConsumeStatus

from webhook.utils import log_init


class Consumer:

    def callback(self, msg):
        print(msg.id, msg.body)
        return ConsumeStatus.CONSUME_SUCCESS

    def consume(self):
        consumer = PushConsumer('CID_XXX')
        consumer.set_name_server_address('172.16.188.2:9876')
        consumer.subscribe('YOUR-TOPIC', self.callback)
        consumer.start()

        while True:
            time.sleep(3600)
        consumer.shutdown()


if __name__ == '__main__':
    log_init()
    consumer = Consumer()
    consumer.consume()
