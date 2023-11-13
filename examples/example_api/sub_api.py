from base import base_meth
from nested.nested import nested_method


edit_num = 9


def sub_api():
    return (
        f"sub api edit is indeed working: {edit_num} "
        + base_meth()
        + "\n\n"
        + nested_method()
    )
