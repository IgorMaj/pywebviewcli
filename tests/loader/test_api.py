import sys

from pywebviewcli.loader.api import unload_module, unload_user_api


def test_unload_module():
    import this

    module_count = len(sys.modules.keys())
    unload_module("this")
    new_module_count = len(sys.modules.keys())
    assert module_count == new_module_count + 1


class MockedWindow:
    def __init__(self) -> None:
        self._functions = {"reload_all": lambda: 1, "test": lambda: 0}


def test_unload_user_api():
    mocked_window = MockedWindow()
    assert len(mocked_window._functions) > 1
    unload_user_api(mocked_window)
    assert len(mocked_window._functions) == 1
