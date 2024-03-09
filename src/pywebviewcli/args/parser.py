import argparse
import os
import sys
from types import NoneType
from dotenv import load_dotenv
from .constants import (
    API_PATH_ARG_HELP,
    DEBUG_PORT_ARG_HELP,
    ENV_PATH_ARG_HELP,
    INPUT_DIR_ARG_HELP,
    INPUT_PATH_REQUIRED,
    OUTPUT_DIR_ARG_HELP,
    PACKAGE_JSON_PATH_HELP,
    PROGRAM_VERSION,
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
DEFAULT_OUT_DIR = "./dist"
DEFAULT_PACKAGE_JSON_PATH = "./package.json"


class ConfigParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            prog=PROGRAM_NAME,
            description=PROGRAM_DESCRIPTION,
            epilog=PROGRAM_EPILOG,
        )
        subparsers = self.parser.add_subparsers(
            title="Subcommands", dest="subcommand", help="Subcommand help"
        )
        dev_parser = subparsers.add_parser("dev")

        dev_parser.add_argument("-t", "--title", help=TITLE_ARG_HELP)
        dev_parser.add_argument("-u", "--url", help=URL_ARG_HELP)
        dev_parser.add_argument("-ap", "--api-path", help=API_PATH_ARG_HELP)
        dev_parser.add_argument("-wt", "--wait-timeout", help=WAIT_TIMEOUT_ARG_HELP)
        dev_parser.add_argument("-dp", "--debug-port", help=DEBUG_PORT_ARG_HELP)
        dev_parser.add_argument("-ep", "--env-path", help=ENV_PATH_ARG_HELP)

        build_parser = subparsers.add_parser("build")
        build_parser.add_argument("-t", "--title", help=TITLE_ARG_HELP)
        build_parser.add_argument("-ep", "--env-path", help=ENV_PATH_ARG_HELP)
        build_parser.add_argument("-ip", "--input-dir", help=INPUT_DIR_ARG_HELP)
        build_parser.add_argument("-op", "--out-dir", help=OUTPUT_DIR_ARG_HELP)
        build_parser.add_argument("-ap", "--api-path", help=API_PATH_ARG_HELP)

        init_parser = subparsers.add_parser("init")
        init_parser.add_argument(
            "-pjp", "--package-json-path", help=PACKAGE_JSON_PATH_HELP
        )
        init_parser.add_argument("-ep", "--env-path", help=ENV_PATH_ARG_HELP)

        self.parser.add_argument(
            "-v",
            "--version",
            action="version",
            version=PROGRAM_VERSION,
        )
        self._args = None

    def parse_args(self) -> None:
        self._args = self.parser.parse_args()
        try:
            if self._args.env_path:
                self._load_env()
        except AttributeError:
            self.parser.print_help()
            sys.exit(0)

    def _load_env(self):
        load_dotenv(self._args.env_path)

    def command(self):
        return self._args.subcommand

    def title(self) -> str:
        return self._args.title or os.getenv("TITLE") or DEFAULT_TITLE

    def url(self) -> str:
        return self._args.url or os.getenv("URL") or DEFAULT_URL

    def api_path(self) -> str | NoneType:
        return self._args.api_path or os.getenv("API_PATH") or None

    def wait_timeout(self) -> int:
        return int(
            self._args.wait_timeout or os.getenv("WAIT_TIMEOUT") or DEFAULT_WAIT_TIMEOUT
        )

    def debug_port(self) -> int | None:
        ret_val = self._args.debug_port or os.getenv("DEBUG_PORT") or None
        return int(ret_val) if ret_val is not None else None

    def input_dir(self) -> str | NoneType:
        return (
            self._args.input_dir
            or os.getenv("INPUT_DIR")
            or sys.exit(print(INPUT_PATH_REQUIRED))
        )

    def out_dir(self) -> str:
        return self._args.out_dir or os.getenv("OUT_DIR") or DEFAULT_OUT_DIR

    def package_json_path(self) -> str:
        return (
            self._args.package_json_path
            or os.getenv("PACKAGE_JSON_PATH")
            or DEFAULT_PACKAGE_JSON_PATH
        )


config_parser = ConfigParser()
