import os
import pathlib
import shutil
import tempfile
from src.pywebviewcli.file_manager.methods import (
    backup_file,
    create_temp_dir,
    file_exists,
    generate_id,
    generate_unique_app_name,
    generate_unique_static_name,
    get_absolute_path,
    get_parent_path,
    remove_dir,
    write_file,
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


def test_write_file():
    temp_path = create_temp_dir()
    test_file_path = f"{temp_path}/foo/bar/test.txt"
    content = "test"
    write_file(test_file_path, content)
    with open(test_file_path, "r") as file:
        assert content == file.read()

    shutil.rmtree(temp_path)


def test_remove_dir():
    temp_path = create_temp_dir()
    assert pathlib.Path(temp_path).exists()
    remove_dir(temp_path)
    assert not pathlib.Path(temp_path).exists()


def test_get_absolute_path():
    file_path = "./test_methods.py"
    abs_path = get_absolute_path(file_path)
    assert abs_path != file_path
    assert len(abs_path) > len(file_path)


def test_backup_file():
    # prepare file
    fp = tempfile.NamedTemporaryFile()
    fp.write(b"Test")
    filename = fp.name
    backup_file(filename)

    fp.close()

    # test backup
    assert pathlib.Path(f"{filename}.bak").exists()

    # cleanup
    os.remove(f"{filename}.bak")


def test_file_exists():
    # Prepare file
    fp = tempfile.NamedTemporaryFile()
    fp.write(b"Test")
    filename = fp.name

    assert file_exists(filename)

    # closing should delete it
    fp.close()

    assert not file_exists(filename)

    # file which never existed at all
    assert not file_exists(f"{filename}.garbage")
