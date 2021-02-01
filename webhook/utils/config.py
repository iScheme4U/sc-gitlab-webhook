"""Configurations

Copyright (c) 2021 Scott Lau
"""

import logging

from scconfig.config import Config

from webhook.configs.default import DEFAULT_CONFIG

# =========================================
#       INSTANCES
# --------------------------------------
try:
    config = Config.create(project_name="sc-gitlab-webhook", defaults=DEFAULT_CONFIG)
except Exception as error:
    logging.getLogger(__name__).exception("failed to read configuration", exc_info=error)
