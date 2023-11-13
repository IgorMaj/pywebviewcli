from nested.nested import nested_method
from sub_api import sub_api


def test():
    return "test 1"


def test2():
    return "test 2"


def test3():
    return "test 3"


def test4():
    return "test 4"


def sub_api_call():
    return sub_api()


def nested_call():
    return nested_method()
