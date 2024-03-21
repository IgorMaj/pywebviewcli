import os
from pathlib import Path
import shutil
import tempfile
import pytest
from src.pywebviewcli.framework.vue import get_vue_init_file_path


def test_get_vue_init_file_path():
    temp_dir = tempfile.mkdtemp()

    # Directory is empty, no main.js/main.ts file to be found, hence the Exception
    with pytest.raises(Exception) as e_info:
        get_vue_init_file_path(temp_dir)
    print(e_info)

    # Both paths should exist once we write them
    paths_to_check = [f"{temp_dir}/src/main.js", f"{temp_dir}/src/main.ts"]

    for full_path in paths_to_check:
        # make src directory
        os.makedirs(str(Path(full_path).parent.absolute()), exist_ok=True)
        with open(full_path, "w") as file:
            file.write("test")

        # it should find the value of full path first
        assert get_vue_init_file_path(temp_dir) == full_path
        # cleanup, so because we can't have main.js and main.ts in the same dir
        os.remove(full_path)

    # Cleanup
    shutil.rmtree(temp_dir)
