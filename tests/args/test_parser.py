import os
from pywebviewcli.args.parser import ConfigParser


class NoneArgs:
    def __init__(self):
        self.title = None
        self.url = None
        self.api_path = None
        self.wait_timeout = None


# priority 1, passed args
def test_args():
    class MockedArgs:
        def __init__(self):
            self.title = "test title"
            self.url = "https://test.com"
            self.api_path = "testpath"
            self.wait_timeout = 5

    parser = ConfigParser()
    mocked_args = MockedArgs()
    parser._args = mocked_args

    assert parser.title() == mocked_args.title
    assert parser.url() == mocked_args.url
    assert parser.api_path() == mocked_args.api_path
    assert parser.wait_timeout() == mocked_args.wait_timeout


# priority 2, env variables if none passed
def test_envs():
    os.environ["TITLE"] = "test title"
    os.environ["URL"] = "https://test.com"
    os.environ["API_PATH"] = "testpath"
    os.environ["WAIT_TIMEOUT"] = "5"

    parser = ConfigParser()
    parser._args = NoneArgs()

    assert parser.title() == os.environ["TITLE"]
    assert parser.url() == os.environ["URL"]
    assert parser.api_path() == os.environ["API_PATH"]
    assert parser.wait_timeout() == int(os.environ["WAIT_TIMEOUT"])

    del os.environ["TITLE"]
    del os.environ["URL"]
    del os.environ["API_PATH"]
    del os.environ["WAIT_TIMEOUT"]


# priority 3, if no args or variables are provided, fall back to defaults
def test_defaults():
    parser = ConfigParser()
    parser._args = NoneArgs()

    assert parser.title() == "App"
    assert parser.url() == "http://localhost"
    assert parser.api_path() == None
    assert parser.wait_timeout() == 10
