"""logging utilities

Copyright (c) 2021 Scott Lau
"""

import logging
import logging.handlers
import os
import sys
from logging.handlers import TimedRotatingFileHandler

from webhook.utils import ensure_dir

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
LOG_FILE_NAME = os.environ.get('LOG_FILE_NAME', 'logs/sys.log')
LOG_FORMAT = os.environ.get('LOG_FORMAT', '%(asctime)s [%(levelname)s]: %(message)s')


def log_init():
    ensure_dir(LOG_FILE_NAME)
    root_logger = logging.getLogger()
    root_logger.setLevel(LOG_LEVEL)
    file_handler = TimedRotatingFileHandler(LOG_FILE_NAME, when='D', interval=1, backupCount=32)
    formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
