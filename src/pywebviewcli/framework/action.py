from react import get_react_init_file_path, patch_react_env_file
from templates.generate import generate_init_template


def react_action(project_dir_path: str):
    init_template = generate_init_template()
    react_init_file_path = get_react_init_file_path(project_dir_path)
    # Read the content of the file
    with open(react_init_file_path, "r") as file:
        content = file.read()

    # Find the last occurrence of "import"
    import_index = content.rfind("import")

    if import_index == -1:
        # If "import" not found, just append at the end
        content = init_template + "\n" + content
    else:
        # Insert the text after the last import statement
        insert_index = content.find("\n", import_index) + 1
        content = content[:insert_index] + init_template + "\n" + content[insert_index:]

    # Write the modified content back to the file
    with open(react_init_file_path, "w") as file:
        file.write(content)

    patch_react_env_file()


def angular_action(project_dir_path: str):
    pass


def vue_action(project_dir_path: str):
    pass


action_map = {"react": react_action, "angular": angular_action, "vue": vue_action}


def do_additional_platform_init(framework_name: str, project_dir_path: str):
    action_map[framework_name](project_dir_path)
