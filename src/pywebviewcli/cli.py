# Path Start (Necessary so it works as a wheel)
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# Path End

from args.parser import config_parser
from commands.build import build_command
from commands.dev import dev_command


command_map = {
    "dev": lambda parser: dev_command(parser),
    "build": lambda parser: build_command(parser),
}


def main():
    config_parser.parse_args()
    if config_parser.command() not in command_map:
        raise Exception(f"Unknown command: {config_parser.command()}")

    command_map[config_parser.command()](config_parser)


if __name__ == "__main__":
    main()
