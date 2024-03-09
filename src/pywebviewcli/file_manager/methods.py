import os
from pathlib import Path
import shutil
import tempfile
import uuid
import json


def generate_id() -> str:
    return str(uuid.uuid4()).replace("-", "")


def generate_unique_app_name():
    return f"app_{generate_id()}.py"


def generate_unique_static_name():
    return f"static_{generate_id()}"


def get_absolute_path(path: str | None):
    if not path:
        return path
    return str(Path(path).absolute())


def get_parent_path(path: str):
    return str(Path(path).parent.absolute())


def create_temp_dir():
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def copy_dir(source_path, destination_path):
    shutil.copytree(source_path, destination_path, dirs_exist_ok=True)


def write_file(file_path: str, content: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")


def move_dir(source_path, destination_path):
    shutil.move(source_path, destination_path)


def remove_dir(temp_dir):
    try:
        shutil.rmtree(temp_dir)
    except FileNotFoundError:
        # Ignore file already being removed
        pass
    except Exception as error:
        print(f"Warning, failed to remove {temp_dir}: {error}")


def read_json_file(path: str) -> dict:
    with open(path, "r") as json_file:
        return json.load(json_file)


def write_json_file(path: str, content: dict):
    with open(path, "w") as json_file:
        json.dump(content, json_file, indent=4)


# backups file to the same dir, just adds .bak extension
def backup_file(path: str):
    shutil.copyfile(path, f"{path}.bak")


def file_exists(path: str):
    return Path(path).exists()


def read_env_file(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


def write_env_file(file_path: str, lines: list[str]):
    with open(file_path, "w") as f:
        f.writelines(lines)
