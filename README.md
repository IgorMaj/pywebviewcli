# PyWebViewCLI
## Overview
[pywebview](https://github.com/r0x0r/pywebview) is a lightweight cross-platform wrapper around a webview component that enables the user to  to display HTML content in its own native GUI window. It's fully featured, allowing for full integration between _Python_ and _JS_ technologies. However, while using it, I found the development workflow a bit slow (no automatic python code reload, python debug support or easy builtin way to build everything). That's how the idea for this tool was born.

_PyWebViewCLI_ is a command-line interface (CLI) tool designed to enhance the development experience with pywebview and various frontend frameworks/setups. It facilitates a seamless workflow by supporting both command line arguments and environment variables. The tool currently offers two main subcommands: _dev_ and _build_. Each subcommand has its own set of options and functionalities to streamline the development and build processes.

## Installation
Before using PyWebViewCLI, ensure you have Python installed on your system. You can install PyWebViewCLI using `pip`:

```bash
pip install git+ssh://git@github.com/IgorMaj/pywebviewcli.git
```
It should automatically take care of any dependencies.

## Usage
You can run the following commands to see how the tool works:

```bash
pywebviewcli --help
```

```bash
pywebviewcli dev --help
```

```bash
pywebviewcli build --help
```

## Features
- Full _pywebview_ integration (dev tools automatically enabled in dev mode)
- Reload both python and JS code at once (pressing `F5` should do the trick)
- Debug Adapter Protocol server support by specifying a `DEBUG_PORT`. This can easily be integrated with various IDEs such as VSCode
- [Pyinstaller](https://github.com/pyinstaller/pyinstaller) is used for application packaging i.e `build` command

## Feedback
We welcome any feedback on PyWebViewCLI. As the tool is currently in early development, your insights and suggestions will be invaluable in improving its functionality and user experience. Feel free to report issues or contribute to the development of this tool on this GitHub repository.
Thank you for using PyWebViewCLI!
