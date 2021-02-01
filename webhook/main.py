"""The Main routine

Copyright (c) 2021 Scott Lau
"""

import logging
from sys import exc_info

from webhook.utils import config, log_init
from webhook import server


class Runner(object):
    def __init__(self):
        pass

    def run(self):
        dev_mode = False
        try:
            dev_mode = config.get("dev.dev_mode")
        except AttributeError:
            pass
        logging.info('program is running in development mode: {}'.format(dev_mode))
        server_ip = config.get("server.ip")
        server_port = config.get("server.port")
        server.run(host=server_ip, port=server_port)
        return 0


def main():
    try:
        log_init()
        state = Runner().run()
    except Exception:
        logging.error('An error occurred.', exc_info=exc_info())
    else:
        return state

    return 0


if __name__ == '__main__':
    main()
