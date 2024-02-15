# Additional react action
from file_manager.methods import file_exists


def get_react_init_file_path(project_dir_path: str) -> str:
    index_base_path = f"{project_dir_path}/src/index"
    if file_exists(f"{index_base_path}.jsx"):
        return f"{index_base_path}.jsx"
    elif file_exists(f"{index_base_path}.tsx"):
        return f"{index_base_path}.tsx"
    elif file_exists(f"{index_base_path}.js"):
        return f"{index_base_path}.js"
    elif file_exists(f"{index_base_path}.ts"):
        return f"{index_base_path}.ts"
    raise Exception("TODO: No react init file")


init_template = """
const initPyWebView = () => {
  return new Promise((resolve) => {
    window.addEventListener("pywebviewready", () => {
      resolve();
    });
  });
};
await initPyWebView();
"""


def react_action(project_dir_path: str):
    react_init_file_path = get_react_init_file_path(project_dir_path)
    # Read the content of the file
    with open(react_init_file_path, "r") as file:
        content = file.read()

    # Find the last occurrence of "import"
    import_index = content.rfind("import")

    if import_index == -1:
        # If "import" not found, just append at the end
        content += "\n" + init_template
    else:
        # Insert the text after the last import statement
        insert_index = content.find("\n", import_index) + 1
        content = content[:insert_index] + init_template + "\n" + content[insert_index:]

    # Write the modified content back to the file
    with open(react_init_file_path, "w") as file:
        file.write(content)


def angular_action(project_dir_path: str):
    pass


def vue_action(project_dir_path: str):
    pass


action_map = {"react": react_action, "angular": angular_action, "vue": vue_action}


def do_additional_platform_init(framework_name: str, project_dir_path: str):
    action_map[framework_name](project_dir_path)
