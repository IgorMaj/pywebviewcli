import os
import tempfile
from src.pywebviewcli.framework.react import get_react_init_file_path


def test_get_react_init_file_path():
    def test_file(fname: str):
        with tempfile.TemporaryDirectory() as project_root:
            # create dir tree (project root/src)
            os.mkdir(f"{project_root}/src")
            # create index file
            with open(f"{project_root}/src/{fname}", "w") as file:
                file.write("test")
                # test whether the method can find the file
                assert (
                    get_react_init_file_path(project_root)
                    == f"{project_root}/src/{fname}"
                )

    # Test all combinations
    test_file("index.jsx")
    test_file("index.tsx")
    test_file("index.js")
    test_file("index.ts")
