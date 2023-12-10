PROGRAM_NAME = """pywebviewcli"""
PROGRAM_DESCRIPTION = """This cli tool aims to provide a smooth development experience with pywebview 
and frontend framework/setup of your choice. It supports command line arguments as well as environment variables. Commands below (build, dev...) have their own --help items. For example you can run
'pywebviewcli dev --help' to see more details:
"""
PROGRAM_EPILOG = (
    """Any feedback is welcome. This tool is still under early development."""
)

TITLE_ARG_HELP = """Sets the webview window title, equivalent env variable is TITLE. Default: "App". """
URL_ARG_HELP = """Sets the webview window url, equivalent env variable is URL. Default: "http://localhost". """
API_PATH_ARG_HELP = """Path to main file of the python code. The file's parent directory is considered the source root. 
The file can use library, absolute and relative imports. Default: None."""
ENV_PATH_ARG_HELP = """Specify path to an .env file which contains argument environment variables. Optional."""
WAIT_TIMEOUT_ARG_HELP = """The cli will wait for up x seconds for the frontend server to become available before starting the webview.
If the server starts up before the timeout, the webview will appear.
Set to 0 to disable. Default: 10 secs."""
DEBUG_PORT_ARG_HELP = """Start a Debug Adapter Protocol server on the specified port. Equivalent env variable is DEBUG_PORT. Default: None (no debug server will start up)"""
INPUT_DIR_ARG_HELP = """Path to static directory containing index.html and optionally all html css and js files. Equivalent env variable is INPUT_DIR. Default: None"""
OUTPUT_DIR_ARG_HELP = """Path to destination directory for compiled (packaged) application. Equivalent env variable is OUT_DIR. Default: ./dist"""
PROGRAM_VERSION = "0.0.4"
