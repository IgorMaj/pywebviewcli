from framework.common import parse_app_init_file
from file_manager.methods import file_exists
from templates.generate import generate_init_template


def get_vue_init_file_path(project_dir_path: str) -> str:
    potential_vue_init_paths = [
        f"{project_dir_path}/src/main.ts",
        f"{project_dir_path}/src/main.js",
    ]
    for full_path in potential_vue_init_paths:
        if file_exists(full_path):
            return full_path

    raise Exception("Error: No vue init file found.")


def vue_action(project_dir_path: str):
    vue_init_path = get_vue_init_file_path(project_dir_path)
    imports, main_code = parse_app_init_file(vue_init_path)
    init_template_content = generate_init_template(imports=imports, main_code=main_code)

    # Write the modified content back to the file
    with open(vue_init_path, "w") as file:
        file.write(init_template_content)
