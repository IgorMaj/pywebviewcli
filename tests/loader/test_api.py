import sys
import threading
import time

from pywebviewcli.loader.api import (
    get_methods,
    is_current_thread,
    is_main_thread,
    stop_background_threads,
    terminate_thread,
    unload_module,
    unload_user_api,
)


def test_unload_module():
    import this

    module_count = len(sys.modules.keys())
    unload_module("this")
    new_module_count = len(sys.modules.keys())
    assert module_count == new_module_count + 1


def test_unload_user_api():
    class MockedWindow:
        def __init__(self) -> None:
            self._functions = {"reload_all": lambda: 1, "test": lambda: 0}

    mocked_window = MockedWindow()
    assert len(mocked_window._functions) > 1
    unload_user_api(mocked_window)
    assert len(mocked_window._functions) == 1


def test_get_methods():
    import types

    class DynamicModule(types.ModuleType):
        a = lambda x: x * 2
        b = lambda y: y

    assert len(get_methods(DynamicModule)) == 2


def test_is_main_thread():
    assert is_main_thread(threading.main_thread()) == True
    assert is_main_thread(threading.Thread()) == False


def test_is_current_thread():
    assert is_current_thread(threading.current_thread()) == True
    assert is_current_thread(threading.Thread()) == False


def test_terminate_thread():
    def forever_func():
        try:
            while True:
                pass
        except:  # python dynamically throws an exception here
            pass

    thread = threading.Thread(target=forever_func)
    thread.start()
    assert thread.is_alive()
    terminate_thread(thread)
    time.sleep(0.1)
    assert not thread.is_alive()


def test_stop_background_threads():
    def forever_func():
        try:
            while True:
                pass
        except:  # python dynamically throws an exception here
            pass

    user_thread_count = 2
    for _ in range(user_thread_count):
        thread = threading.Thread(target=forever_func)
        thread.start()

    time.sleep(0.1)
    current_thread_count = threading.active_count()
    stop_background_threads()
    time.sleep(0.1)
    assert current_thread_count - user_thread_count == threading.active_count()
