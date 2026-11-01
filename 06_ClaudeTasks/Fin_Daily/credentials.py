"""Load public settings and inject credentials from the running environment."""

import json
import os


def load_config(config_path, environ=None):
    """Never use or save legacy credentials stored in a configuration file."""
    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)
    environment = os.environ if environ is None else environ
    rss = config.setdefault("rss", {})
    rss["lingowhale_username"] = environment.get("LINGOWHALE_USERNAME", "")
    rss["lingowhale_password"] = environment.get("LINGOWHALE_PASSWORD", "")
    return config
