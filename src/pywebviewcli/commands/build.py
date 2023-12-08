from pathlib import Path
from jinja2 import Environment, FileSystemLoader
import tempfile
import os
import shutil

from args.parser import ConfigParser


def get_parent_path(path: str):
    return str(Path(path).parent.absolute())


def generate_app_template(api_path: str = None):
    dir_path = get_parent_path(get_parent_path(__file__))
    env = Environment(loader=FileSystemLoader(dir_path))
    template = env.get_template(f"./templates/app.j2")
    template_vars = {}

    if api_path:
        # get name without extension (.py)
        api_name = Path(api_path).stem
        template_vars["api_name"] = api_name

    return template.render(template_vars)


def create_app(app_template_content):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, "app.py")
    with open(file_path, "w") as file:
        file.write(app_template_content)

    return temp_dir


def copy_dir(source_path, destination_path):
    shutil.copytree(source_path, destination_path)


def move_dir(source_path, destination_path):
    shutil.move(source_path, destination_path)


def remove_dir(temp_dir):
    try:
        shutil.rmtree(temp_dir)
    except Exception as error:
        print(error)


def package_app(temp_dir):
    os.chdir(temp_dir)
    os.system("pyinstaller --add-data static:static app.py")


def build_command(config_parser: ConfigParser):
    content = generate_app_template(config_parser.api_path())
    temp_dir = create_app(content)

    copy_dir(config_parser.input_dir(), f"{temp_dir}/static")

    if config_parser.api_path():
        api_dir = get_parent_path(config_parser.api_path())
        copy_dir(api_dir, f"{temp_dir}/api")

    package_app(temp_dir)

    remove_dir(config_parser.out_dir())
    move_dir(f"{temp_dir}/dist/app", config_parser.out_dir())
    remove_dir(temp_dir)
