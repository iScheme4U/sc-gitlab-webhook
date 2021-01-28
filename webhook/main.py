"""The Main routine

Copyright (c) 2021 Scott Lau
"""

from sys import stdout, stderr
from traceback import print_exc

from webhook.config import config


class Runner(object):
    def __init__(self):
        pass

    def run(self):
        dev_mode = False
        try:
            dev_mode = config.get("dev.dev_mode")
        except:
            pass
        print('program is running in development mode: {}'.format(dev_mode))
        return 0


def main():
    try:
        state = Runner().run()
    except Exception:
        # Flush the problems we have printed so far to avoid the traceback appearing in between them.
        stdout.flush()
        print(file=stderr)
        print('An error occurred.', file=stderr)
        print_exc()
    else:
        return state;

    return 0
