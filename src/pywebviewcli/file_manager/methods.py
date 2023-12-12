from pathlib import Path
import shutil
import tempfile
import uuid


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


def write_file_to_directory(file_path: str, content: str):
    try:
        with open(file_path, "w") as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred: {e}")


def move_dir(source_path, destination_path):
    shutil.move(source_path, destination_path)


def remove_dir(temp_dir):
    try:
        shutil.rmtree(temp_dir)
    except Exception as error:
        print(f"Warning, failed to remove {temp_dir}: {error}")
