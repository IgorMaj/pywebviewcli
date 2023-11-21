import argparse
import os
from types import NoneType

from dotenv import load_dotenv

from .constants import (
    API_PATH_ARG_HELP,
    ENV_PATH_ARG_HELP,
    WAIT_TIMEOUT_ARG_HELP,
    PROGRAM_DESCRIPTION,
    PROGRAM_EPILOG,
    PROGRAM_NAME,
    TITLE_ARG_HELP,
    URL_ARG_HELP,
)

DEFAULT_URL = "http://localhost"
DEFAULT_TITLE = "App"
DEFAULT_WAIT_TIMEOUT = 10  # secs


class ConfigParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog=PROGRAM_NAME,
            description=PROGRAM_DESCRIPTION,
            epilog=PROGRAM_EPILOG,
        )
        self.parser.add_argument("-t", "--title", help=TITLE_ARG_HELP)
        self.parser.add_argument("-u", "--url", help=URL_ARG_HELP)
        self.parser.add_argument("-ap", "--api-path", help=API_PATH_ARG_HELP)
        self.parser.add_argument("-wt", "--wait-timeout", help=WAIT_TIMEOUT_ARG_HELP)
        self.parser.add_argument("-ep", "--env-path", help=ENV_PATH_ARG_HELP)
        self._args = None

    def parse_args(self) -> None:
        self._args = self.parser.parse_args()
        if self._args.env_path:
            self._load_env()

    def _load_env(self):
        load_dotenv(self._args.env_path)

    def title(self) -> str:
        return self._args.title or os.getenv("TITLE") or DEFAULT_TITLE

    def url(self) -> str:
        return self._args.url or os.getenv("URL") or DEFAULT_URL

    def api_path(self) -> str | NoneType:
        return self._args.api_path or os.getenv("API_PATH") or None

    def wait_timeout(self):
        return int(
            self._args.wait_timeout or os.getenv("WAIT_TIMEOUT") or DEFAULT_WAIT_TIMEOUT
        )


config_parser = ConfigParser()
