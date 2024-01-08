import sys
from pathlib import Path

# to be able to see args and other modules which generate_module relies on
sys.path.insert(
    0,
    str(Path(f"{Path(__file__).parent}/../../src/pywebviewcli").absolute()),
)
import src.pywebviewcli.templates.generate as generate_module


def test_generate_app_template():
    template_str = generate_module.generate_app_template()
    assert '"App"' in template_str
    assert "static/" in template_str


def test_generate_app_template_api_path():
    template_str = generate_module.generate_app_template(
        api_path="./api/example.py",
    )
    assert "import example" in template_str


def test_generate_app_template_title():
    template_str = generate_module.generate_app_template(
        app_title="Custom Title",
    )
    assert '"Custom Title"' in template_str


def test_generate_app_template_static_dirname():
    template_str = generate_module.generate_app_template(
        static_dirname="static_custom",
    )
    assert "static_custom/" in template_str


def test_generate_cli_env_template():
    template_str = generate_module.generate_cli_env_template(
        port=4000,
    )
    assert "localhost:4000" in template_str


def test_generate_api_template():
    template_str = generate_module.generate_api_template()
    assert "def hello" in template_str
