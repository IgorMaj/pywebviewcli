import importlib.util
import os
from pathlib import Path
import sys
from types import ModuleType

import webview


def get_api_root_dir_path(api_file_path: str):
    return str(Path(api_file_path).parent.absolute())


# Allows our api module to relative import other modules
# https://stackoverflow.com/questions/37808866/proper-way-to-dynamically-import-a-module-with-relative-imports
def add_api_root_to_path(api_file_path: str):
    root_path = get_api_root_dir_path(api_file_path)
    sys.path.append(root_path)


def get_absolute_module_path(module: ModuleType):
    try:
        return os.path.abspath(module.__file__)
    except:
        # builtin modules should probably return this
        return ""


def load_module_from_file(path: str):
    spec = importlib.util.spec_from_file_location(
        name="api.module",
        location=path,
        submodule_search_locations=["example_api"],
    )
    loaded_module = importlib.util.module_from_spec(spec)
    sys.modules["api.module"] = loaded_module
    spec.loader.exec_module(loaded_module)
    return loaded_module


def unload_module(name: str):
    del sys.modules[name]


def reload_window_api(window: webview.Window, api_file_path: str):
    root_dir_path = get_api_root_dir_path(api_file_path)
    module_keys_to_unload = []
    for key in sys.modules.keys():
        absolute_module_path = get_absolute_module_path(sys.modules[key])
        if absolute_module_path.startswith(root_dir_path):
            module_keys_to_unload.append(key)

    for key in module_keys_to_unload:
        unload_module(key)

    window._js_api = load_module_from_file(api_file_path)
