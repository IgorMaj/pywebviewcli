PROGRAM_DESCRIPTION = """This cli tool aims to provide a smooth development experience with pywebview 
and frontend framework/setup of your choice. You can use the options below to pass arguments, an env path 
or in-memory environment variables which correspond to the arguments:
"""
PROGRAM_EPILOG = """Any feedback is welcome. This tool is still under development."""

TITLE_ARG_HELP = """Sets the webview window title, equivalent env variable is TITLE. Default: "App". """
URL_ARG_HELP = """Sets the webview window url, equivalent env variable is URL. Default: "http://localhost". """
API_PATH_ARG_HELP = """Path to main file of the python code. The file's parent directory is considered the source root. 
The file can use both library and relative imports. Default: None."""
ENV_PATH_ARG_HELP = (
    """Specify path to an .env file which contains arg env variables. Optional."""
)
