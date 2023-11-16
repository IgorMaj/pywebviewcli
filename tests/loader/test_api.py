import sys

from pywebviewcli.loader.api import get_methods, unload_module, unload_user_api


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
