import webview
from js.methods import add_reload_listener, reload_window
from loader.api import (
    add_api_root_to_path,
    load_module_api,
    reload_window_api,
)
from args.parser import config_parser


def main():
    config_parser.parse_args()
    add_reload_listener()

    if config_parser.api_path():
        add_api_root_to_path(config_parser.api_path())

    window = webview.create_window(title=config_parser.title(), url=config_parser.url())

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
