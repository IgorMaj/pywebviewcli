from subprocess import Popen
import os

from args.parser import ConfigParser
from file_manager.methods import (
    copy_dir,
    create_temp_dir,
    generate_unique_app_name,
    generate_unique_static_name,
    get_absolute_path,
    get_parent_path,
    move_dir,
    remove_dir,
    write_file,
)

from templates.generate import generate_app_template


def package_app(
    temp_dir: str,
    unique_app_filename: str = "app.py",
    unique_static_dirname: str = "static",
):
    os.chdir(temp_dir)
    Popen(
        f"pyinstaller --add-data {unique_static_dirname}:{unique_static_dirname} {unique_app_filename} --name app",
        shell=True,
    ).wait()


def build_command(config_parser: ConfigParser):
    absolute_input_path = get_absolute_path(config_parser.input_dir())
    absolute_output_path = get_absolute_path(config_parser.out_dir())
    unique_app_filename = generate_unique_app_name()
    unique_static_dirname = generate_unique_static_name()
    temp_dir = create_temp_dir()
    try:
        copy_dir(absolute_input_path, f"{temp_dir}/{unique_static_dirname}")

        if config_parser.api_path():
            api_dir = get_parent_path(config_parser.api_path())
            copy_dir(api_dir, temp_dir)

        content = generate_app_template(
            config_parser.api_path(), unique_static_dirname, config_parser.title()
        )
        write_file(f"{temp_dir}/{unique_app_filename}", content)

        package_app(temp_dir, unique_app_filename, unique_static_dirname)

        remove_dir(absolute_output_path)
        move_dir(f"{temp_dir}/dist/app", absolute_output_path)
        remove_dir(temp_dir)
    except Exception as e:
        remove_dir(temp_dir)
        raise e
