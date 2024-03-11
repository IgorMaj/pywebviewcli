from pathlib import Path
from jinja2 import Environment, FileSystemLoader

from file_manager.methods import get_parent_path


def generate_app_template(
    api_path: str = None, static_dirname="static", app_title="App"
) -> str:
    env = Environment(loader=FileSystemLoader(get_parent_path(__file__)))
    template = env.get_template(f"./app.j2")
    template_vars = {}

    if api_path:
        # get name without extension (.py)
        api_name = Path(api_path).stem
        template_vars["api_name"] = api_name

    template_vars["static_dirname"] = static_dirname
    template_vars["app_title"] = app_title

    return template.render(template_vars)


def generate_cli_env_template(port=3000) -> str:
    env = Environment(loader=FileSystemLoader(get_parent_path(__file__)))
    template = env.get_template(f"./cli.env.j2")
    template_vars = {"port": port}
    return template.render(template_vars)


def generate_api_template() -> str:
    env = Environment(loader=FileSystemLoader(get_parent_path(__file__)))
    template = env.get_template(f"./api.py.j2")
    return template.render()


def generate_api_js_template(is_typescript=False) -> str:
    env = Environment(loader=FileSystemLoader(get_parent_path(__file__)))
    template = env.get_template(f"./api.js.j2")
    template_vars = {"is_typescript": is_typescript}
    return template.render(template_vars)


def generate_init_template(imports: str, main_code: str) -> str:
    env = Environment(loader=FileSystemLoader(get_parent_path(__file__)))
    template_vars = {"imports": imports, "main_code": main_code}
    template = env.get_template(f"./init.js.j2")
    return template.render(template_vars)
