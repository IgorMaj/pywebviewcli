import debugpy
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
from args.parser import ConfigParser
from patch.qt import patch_on_load_finished
from patch.gtk import patch_gtk_inspector
from loader.wait import wait_for_server_startup


def dev_command(config_parser: ConfigParser):
    add_reload_listener()
    patch_on_load_finished()
    patch_gtk_inspector()

    if config_parser.api_path():
        add_api_root_to_path(config_parser.api_path())

    if config_parser.debug_port():
        debugpy.listen(config_parser.debug_port())

    if config_parser.wait_timeout():
        wait_for_server_startup(config_parser.url(), config_parser.wait_timeout())

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
