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
