import os
from unittest import mock
from src.pywebviewcli.args.parser import ConfigParser


class NoneArgs:
    def __init__(self):
        self.title = None
        self.url = None
        self.api_path = None
        self.wait_timeout = None
        self.debug_port = None
        # build args
        self.input_dir = None
        self.out_dir = None
        # init args
        self.package_json_path = None


# priority 1, passed args
def test_args():
    class MockedArgs:
        def __init__(self):
            self.title = "test title"
            self.url = "https://test.com"
            self.api_path = "testpath"
            self.wait_timeout = 5
            self.debug_port = 5678
            # build args
            self.input_dir = "./input"
            self.out_dir = "./output"
            # init args
            self.package_json_path = "/tmp/package.json"

    parser = ConfigParser()
    mocked_args = MockedArgs()
    parser._args = mocked_args

    assert parser.title() == mocked_args.title
    assert parser.url() == mocked_args.url
    assert parser.api_path() == mocked_args.api_path
    assert parser.wait_timeout() == mocked_args.wait_timeout
    assert parser.debug_port() == mocked_args.debug_port
    assert parser.input_dir() == mocked_args.input_dir
    assert parser.out_dir() == mocked_args.out_dir
    assert parser.package_json_path() == mocked_args.package_json_path


# priority 2, env variables if none passed
def test_envs():
    os.environ["TITLE"] = "test title"
    os.environ["URL"] = "https://test.com"
    os.environ["API_PATH"] = "testpath"
    os.environ["WAIT_TIMEOUT"] = "5"
    os.environ["DEBUG_PORT"] = "5678"
    os.environ["INPUT_DIR"] = "./input"
    os.environ["OUT_DIR"] = "./output"
    os.environ["PACKAGE_JSON_PATH"] = "/tmp/package.json"

    parser = ConfigParser()
    parser._args = NoneArgs()

    assert parser.title() == os.environ["TITLE"]
    assert parser.url() == os.environ["URL"]
    assert parser.api_path() == os.environ["API_PATH"]
    assert parser.wait_timeout() == int(os.environ["WAIT_TIMEOUT"])
    assert parser.debug_port() == int(os.environ["DEBUG_PORT"])
    assert parser.input_dir() == os.environ["INPUT_DIR"]
    assert parser.out_dir() == os.environ["OUT_DIR"]
    assert parser.package_json_path() == os.environ["PACKAGE_JSON_PATH"]

    del os.environ["TITLE"]
    del os.environ["URL"]
    del os.environ["API_PATH"]
    del os.environ["WAIT_TIMEOUT"]
    del os.environ["DEBUG_PORT"]
    del os.environ["INPUT_DIR"]
    del os.environ["OUT_DIR"]
    del os.environ["PACKAGE_JSON_PATH"]


# priority 3, if no args or variables are provided, fall back to defaults
@mock.patch("sys.exit")
def test_defaults(mock_sys_exit):
    parser = ConfigParser()
    parser._args = NoneArgs()

    assert parser.title() == "App"
    assert parser.url() == "http://localhost"
    assert parser.api_path() == None
    assert parser.wait_timeout() == 10
    assert parser.debug_port() == None

    parser.input_dir()
    mock_sys_exit.assert_called()

    assert parser.out_dir() == "./dist"

    assert parser.package_json_path() == "./package.json"
