from file_manager.methods import file_exists
from templates.generate import generate_init_template


def get_react_init_file_path(project_dir_path: str) -> str:
    index_base_path = f"{project_dir_path}/src/index"
    supported_extensions = ["jsx", "tsx", "js", "ts"]
    for extension in supported_extensions:
        full_path = f"{index_base_path}.{extension}"
        if file_exists(full_path):
            return full_path

    raise Exception("TODO: No react init file")


def read_env_file(file_path: str) -> list[str]:
    with open(file_path, "r") as f:
        lines = f.readlines()
    return lines


def write_env_file(file_path: str, lines: list[str]):
    with open(file_path, "w") as f:
        f.writelines(lines)


def patch_react_env_file():
    env_files = [".env", ".env.local"]
    browser_cmd_template = "BROWSER=None"

    for env_file in env_files:
        if file_exists(env_file):
            file_lines = read_env_file(env_file)
            # Check if BROWSER=None already exists
            if not browser_cmd_template in file_lines:
                file_lines.append(f"{browser_cmd_template}\n")

            write_env_file(env_file, file_lines)
            return

    write_env_file(".env", [f"{browser_cmd_template}\n"])


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
