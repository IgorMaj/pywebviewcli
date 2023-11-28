import webview
from src.js.methods import add_reload_listener, reload_window


def test_reload_window():
    class MockWindow:
        def __init__(self):
            self.js = None

        def evaluate_js(self, new_js):
            self.js = new_js

    mock = MockWindow()
    reload_window(mock)
    assert mock.js == "location.reload();"


def test_add_reload_listener():
    orig_src = webview.js.api.src
    add_reload_listener()
    assert orig_src != webview.js.api.src
    assert "event.key === 'F5'" in webview.js.api.src
    webview.js.api.src = orig_src
