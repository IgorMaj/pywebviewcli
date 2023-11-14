import webview
from pywebviewcli.js.methods import add_reload_listener, reload_window
from pywebviewcli.loader.api import (
    add_api_root_to_path,
    load_module_from_file,
    reload_window_api,
)
from pywebviewcli.args.parser import config_parser


def main():
    config_parser.parse_args()
    add_reload_listener()

    if config_parser.api_path():
        add_api_root_to_path(config_parser.api_path())

    window = webview.create_window(
        title=config_parser.title(),
        url=config_parser.url(),
        js_api=load_module_from_file(config_parser.api_path())
        if config_parser.api_path()
        else None,
    )

    def reload_all():
        if config_parser.api_path():
            reload_window_api(window, config_parser.api_path())
        reload_window(window)

    window.expose(reload_all)
    webview.start(debug=True)


if __name__ == "__main__":
    main()
