import ctypes
import importlib.util
import inspect
import os
from pathlib import Path
import sys
import threading
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


def get_methods(module: ModuleType):
    methods = [
        getattr(module, func)
        for func in dir(module)
        if callable(getattr(module, func)) and inspect.isfunction(getattr(module, func))
    ]
    return methods


def load_module_from_file(path: str):
    spec = importlib.util.spec_from_file_location(name="api.module", location=path)
    loaded_module = importlib.util.module_from_spec(spec)
    sys.modules["api.module"] = loaded_module
    spec.loader.exec_module(loaded_module)
    return loaded_module


def load_module_api(path: str):
    return get_methods(load_module_from_file(path))


def unload_module(name: str):
    del sys.modules[name]


# unloads all user defined api methods
def unload_user_api(window: webview.Window):
    window._functions = {"reload_all": window._functions["reload_all"]}


def is_main_thread(thread: threading.Thread):
    return thread is threading.main_thread()


def is_current_thread(thread: threading.Thread):
    return thread is threading.current_thread()


def terminate_thread(thread):
    if not thread.is_alive():
        return
    thread_id = ctypes.c_long(thread.ident)
    ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))


# api calls which run for a long time/forever spawn a thread, that needs to be killed on reload
# Please bear in mind that this method is also part of an api call, so it runs in a thread of its own
def stop_background_threads():
    for thread in threading.enumerate():
        if not is_main_thread(thread) and not is_current_thread(thread):
            terminate_thread(thread)


def reload_window_api(window: webview.Window, api_file_path: str):
    root_dir_path = get_api_root_dir_path(api_file_path)
    module_keys_to_unload = []
    for key in sys.modules.keys():
        absolute_module_path = get_absolute_module_path(sys.modules[key])
        if absolute_module_path.startswith(root_dir_path):
            module_keys_to_unload.append(key)

    stop_background_threads()
    unload_user_api(window)

    for key in module_keys_to_unload:
        unload_module(key)

    window.expose(*load_module_api(api_file_path))
