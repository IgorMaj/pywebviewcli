import webview

# Path Start (Necessary so it works as a wheel)
import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# Path End

from js.methods import add_reload_listener, reload_window
from loader.api import (
    add_api_root_to_path,
    load_module_api,
    reload_window_api,
)
from args.parser import config_parser
from patch.qt import patch_on_load_finished


def main():
    config_parser.parse_args()
    add_reload_listener()
    patch_on_load_finished()

    if config_parser.api_path():
        add_api_root_to_path(config_parser.api_path())

    window = webview.create_window(
        title=config_parser.title(), url=config_parser.url(), maximized=True
    )

    def reload_all():
        if config_parser.api_path():
            reload_window_api(window, config_parser.api_path())
        reload_window(window)

    if config_parser.api_path():
        window.expose(*load_module_api(config_parser.api_path()))

    window.expose(reload_all)
    webview.start(debug=True)


if __name__ == "__main__":
    main()
