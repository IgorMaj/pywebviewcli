import tempfile

from src.pywebviewcli.framework.common import parse_app_init_file


def test_parse_app_init_file():
    # Prepare
    test_file_content = """import this from that;
    console.log('Test');
    """
    with tempfile.NamedTemporaryFile(mode="w") as temp_file:
        # Setup
        temp_file.write(test_file_content)
        temp_file.flush()
        imports, main_code = parse_app_init_file(temp_file.name)

        # Test
        assert "import this from that" in imports
        assert "console.log('Test');" in main_code
