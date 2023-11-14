import webview
from pywebviewcli.js.methods import add_reload_listener, reload_window


class MockWindow:
    def __init__(self):
        self.js = None
        pass

    def evaluate_js(self, new_js):
        self.js = new_js


def test_reload_window():
    mock = MockWindow()
    reload_window(mock)
    assert mock.js == "location.reload();"


def test_add_reload_listener():
    orig_src = webview.js.api.src
    add_reload_listener()
    assert orig_src != webview.js.api.src
    assert "event.key === 'F5'" in webview.js.api.src
    webview.js.api.src = orig_src
