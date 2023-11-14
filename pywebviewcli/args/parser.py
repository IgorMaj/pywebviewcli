import argparse
import os
from types import NoneType

from dotenv import load_dotenv

from translation.constants import (
    API_PATH_ARG_HELP,
    ENV_PATH_ARG_HELP,
    PROGRAM_DESCRIPTION,
    PROGRAM_EPILOG,
    TITLE_ARG_HELP,
    URL_ARG_HELP,
)

DEFAULT_URL = "http://localhost"
DEFAULT_TITLE = "App"


class ConfigParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog="pyweb-cli",
            description=PROGRAM_DESCRIPTION,
            epilog=PROGRAM_EPILOG,
        )
        self.parser.add_argument("-t", "--title", help=TITLE_ARG_HELP)
        self.parser.add_argument("-u", "--url", help=URL_ARG_HELP)
        self.parser.add_argument("-ap", "--api-path", help=API_PATH_ARG_HELP)
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


config_parser = ConfigParser()
