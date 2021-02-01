import logging

from scconfig.config import Config

from webhook.configs.default import DEFAULT_CONFIG
from .file_utils import ensure_dir
from .log_utils import log_init

# =========================================
#       INSTANCES
# --------------------------------------
try:
    # load configurations
    config = Config.create(project_name="sc-gitlab-webhook", defaults=DEFAULT_CONFIG)
except Exception as error:
    config = {}
    logging.getLogger(__name__).exception("failed to read configuration", exc_info=error)

__all__ = {
    "ensure_dir",
    "log_init",
    "config",
}
