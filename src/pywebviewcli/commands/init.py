# Path Start (Necessary so it works as a wheel)
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# Path End
from args.parser import ConfigParser
from file_manager.methods import (
    backup_file,
    get_parent_path,
    read_json_file,
    write_file,
    write_json_file,
)
from http_manager.npm import get_latest_concurrently_version
from templates.generate import generate_api_template, generate_cli_env_template


def edit_package_json_content(content: dict):
    devDepKey = "devDependencies"
    conc_key = "concurrently"

    scr_key = "scripts"
    start_key = "start"
    dev_key = "dev"
    build_key = "build"

    # init dev dependencies if they're not already present
    if devDepKey not in content:
        content[devDepKey] = {}

    # add concurrently to dev deps, if not already present
    if conc_key not in content[devDepKey]:
        content[devDepKey][conc_key] = get_latest_concurrently_version()
    # Modify commands (namely start, dev and build)
    if scr_key not in content:
        raise Exception("TODO: no scripts section text")

    if start_key in content[scr_key]:
        content[scr_key][
            start_key
        ] = f"concurrently 'pywebviewcli dev -ep ./cli.env' '{content[scr_key][start_key]}'"

    if dev_key in content[scr_key]:
        content[scr_key][
            dev_key
        ] = f"concurrently 'pywebviewcli dev -ep ./cli.env' '{content[scr_key][dev_key]}'"

    if build_key in content[scr_key]:
        content[scr_key][
            build_key
        ] = f"concurrently '{content[scr_key][build_key]}' 'pywebviewcli build -ep ./cli.env'"

    return content


def init_command(config_parser: ConfigParser):
    package_json_path = config_parser.package_json_path()
    project_dir_path = get_parent_path(package_json_path)
    package_json_content = read_json_file(package_json_path)
    backup_file(package_json_path)
    package_json_content = edit_package_json_content(package_json_content)
    write_json_file(package_json_path, package_json_content)

    env_file_content = generate_cli_env_template()
    write_file(f"{project_dir_path}/cli.env", env_file_content)

    api_file_content = generate_api_template()
    write_file(f"{project_dir_path}/python/api.py", api_file_content)
