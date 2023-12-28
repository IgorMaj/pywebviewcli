PROGRAM_NAME = "pywebviewcli"
PROGRAM_DESCRIPTION = """\
This CLI tool aims to enhance the development experience with pywebview 
and your chosen frontend framework/setup. It supports command-line arguments 
and environment variables. Each command (e.g., build, dev) has its own --help option.
For example, you can run 'pywebviewcli dev --help' for more details:
"""
PROGRAM_EPILOG = """\
Any feedback is welcome. This tool is still under early development.
"""

TITLE_ARG_HELP = (
    "Sets the webview window title. Equivalent env variable: TITLE. Default: 'App'."
)
URL_ARG_HELP = "Sets the webview window URL. Equivalent env variable: URL. Default: 'http://localhost'."
API_PATH_ARG_HELP = """\
Path to the main Python file. The file's parent directory is considered the source root. 
The file can use library, absolute, and relative imports. Equivalent env variable: API_PATH. Default: None.
"""
ENV_PATH_ARG_HELP = "Specify the path to an .env file containing argument environment variables. Optional."
WAIT_TIMEOUT_ARG_HELP = """\
CLI waits for up to X seconds for the frontend server to become available before starting the webview.
If the server starts up before the timeout, the webview will appear.
Set to 0 to disable. Equivalent env variable: WAIT_TIMEOUT. Default: 10 seconds.
"""
DEBUG_PORT_ARG_HELP = "Start a Debug Adapter Protocol server on the specified port. Equivalent env variable: DEBUG_PORT. Default: None (no debug server starts)."
INPUT_DIR_ARG_HELP = """\
Path to the static directory containing index.html and optionally all HTML, CSS, and JS files. 
Equivalent env variable: INPUT_DIR. Required via env variable/file or command-line argument. Default: None.
"""
OUTPUT_DIR_ARG_HELP = "Path to the destination directory for the compiled (packaged) application. Equivalent env variable: OUT_DIR. Default: './dist'."

INPUT_PATH_REQUIRED = "Input dir path is required. Please specify it via the command-line argument or environment variables/file. Run 'pywebviewcli build --help' for more details."

PROGRAM_VERSION = "0.0.5"
