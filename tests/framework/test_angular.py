import os
import shutil
import tempfile

import pytest
from src.pywebviewcli.framework.angular import (
    find_nested_key_value,
    get_angular_build_output_path,
    get_angular_init_file_path,
)


def test_find_nested_key_value():
    result = find_nested_key_value(
        {"ok": {"nested": {"prop": "ok"}, "nested2": {"target": "result"}}}, "target"
    )
    assert result == "result"

    result = find_nested_key_value(
        {"ok": {"nested": {"prop": "ok"}, "nested2": {"target": "result"}}},
        "nonExistent",
    )
    assert result is None


def test_get_angular_init_file_path():
    temp_dir = tempfile.mkdtemp()
    # Fails, because there is no ./src/main.ts file
    with pytest.raises(Exception) as e_info:
        get_angular_init_file_path(temp_dir)
    print(e_info)

    # We create ./src/main.ts, so it passes
    full_path = f"{temp_dir}/src/main.ts"
    os.makedirs(os.path.dirname(full_path))
    with open(full_path, "w") as file:
        file.write("test")

    assert get_angular_init_file_path(temp_dir) == full_path

    # Cleanup
    shutil.rmtree(temp_dir)


def test_get_angular_build_output_path():
    temp_dir = tempfile.mkdtemp()

    # angular.json doesn't exist, exception will be thrown
    with pytest.raises(Exception) as e_info:
        get_angular_build_output_path(temp_dir)
    print(e_info)

    # this will find the json, parse it, etc
    full_path = f"{temp_dir}/angular.json"
    with open(full_path, "w") as file:
        file.write(
            """{
                   "key": {
                   "other": "ok",
                    "test": {
                        "outputPath": "testOutputPath"
                    }
                   }
        }"""
        )

    # find outputPath and check its value
    assert get_angular_build_output_path(temp_dir) == "testOutputPath"

    # Cleanup
    shutil.rmtree(temp_dir)
