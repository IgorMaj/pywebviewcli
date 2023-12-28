# PyWebViewCLI
## Overview
[pywebview](https://github.com/r0x0r/pywebview) is a lightweight cross-platform wrapper around a webview component that enables the user to display HTML content in its own native GUI window. It's fully featured, allowing for full integration between _Python_ and _JS_ technologies. However, while using it, I found the development workflow a bit slow (no automatic Python code reload, Python debug support or easy builtin way to build everything). That's how the idea for this tool was born.

_PyWebViewCLI_ is a command-line interface (CLI) tool designed to enhance the development experience with pywebview and various frontend frameworks/setups. It facilitates a seamless workflow by supporting both command line arguments and environment variables. The tool currently offers two main subcommands: _dev_ and _build_. Each subcommand has its own set of options and functionalities to streamline the development and build processes.

## Installation
Before using _PyWebViewCLI_, ensure you have Python installed on your system. You can install PyWebViewCLI using `pip`:

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
### Example Usage
The easiest way to integrate `pywebviewcli` into an `npm` project would be like this:

1. Place an env file in the project root (`pywebview.env`):

```bash
# Development server url, see dev help for more details
URL=http://localhost:3000
# Window title
TITLE=React App!
# Path to python api code, fully reloadable in dev mode (by pressing F5). See help menu entry for more details
API_PATH=./python/api.py
# Debug server port. Can be integrated with various IDEs which allows the developer to debug python code
DEBUG_PORT=5678
# When a FE framework is done building the FE part, it serves as input dir for the cli to package everything
INPUT_DIR=./build
# Final output dir which contains the executable and necessary files
OUT_DIR=./dist
```
2. Next you can modify your `package.json` commands:
```json
...
"scripts": {
    "start": "concurrently --kill-others 'react-scripts start' 'pywebviewcli dev -ep ./pywebview.env'",
    "build": "react-scripts build && pywebviewcli build -ep ./pywebview.env",
    ...
  },
...
```

3. Use the recommended way for your framework to disable automatic browser startup, since `pywebview` will render everything. For React, environment `BROWSER=none` should do the trick. 

4. Wrap your startup logic in a `pywebviewready` listener, since pywebview api (`window.pywebview.api`) is not accessible right away. More details [here](https://github.com/r0x0r/pywebview/issues/378).

```js
window.addEventListener("pywebviewready", () => {
 // ... Your startup logic i.e react.render or similar
});
```


## Features
- Full _pywebview_ integration (dev tools automatically enabled in dev mode)
- Reload both python and JS code at once (pressing `F5` should do the trick)
- Debug Adapter Protocol server support by specifying a `DEBUG_PORT`. This can easily be integrated with various IDEs such as VSCode
- [Pyinstaller](https://github.com/pyinstaller/pyinstaller) is used for application packaging i.e `build` command

## Feedback
Any feedback on PyWebViewCLI is welcome. As the tool is currently in early development, your insights and suggestions will be invaluable in improving its functionality and user experience. Feel free to report issues or contribute to the development of this tool on this GitHub repository.
Thank you for using PyWebViewCLI!
