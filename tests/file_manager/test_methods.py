import pathlib
import shutil
from src.pywebviewcli.file_manager.methods import (
    create_temp_dir,
    generate_id,
    generate_unique_app_name,
    generate_unique_static_name,
    get_parent_path,
)


def test_generate_id():
    generated_id = generate_id()
    assert "-" not in generated_id
    assert len(generated_id) == 32


def test_generate_unique_app_name():
    generated_app = generate_unique_app_name()
    assert generated_app.startswith("app_")
    assert generated_app.endswith(".py")


def test_generate_unique_static_name():
    generated_static = generate_unique_static_name()
    assert generated_static.startswith("static_")


def test_get_parent_path():
    path = "/tmp/ok"
    assert get_parent_path(path) == "/tmp"


def test_create_temp_dir():
    temp_path = create_temp_dir()
    assert pathlib.Path(temp_path).exists()
    shutil.rmtree(temp_path)
    assert not pathlib.Path(temp_path).exists()
