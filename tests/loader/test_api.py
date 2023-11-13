import sys

from loader.api import unload_module


def test_unload_module():
    import this

    module_count = len(sys.modules.keys())
    unload_module("this")
    new_module_count = len(sys.modules.keys())
    assert module_count == new_module_count + 1
