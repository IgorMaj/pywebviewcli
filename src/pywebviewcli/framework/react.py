from file_manager.methods import file_exists, read_env_file, write_env_file
from templates.generate import generate_init_template


def get_react_init_file_path(project_dir_path: str) -> str:
    index_base_path = f"{project_dir_path}/src/index"
    supported_extensions = ["jsx", "tsx", "js", "ts"]
    for extension in supported_extensions:
        full_path = f"{index_base_path}.{extension}"
        if file_exists(full_path):
            return full_path

    raise Exception("Error: No react init file found.")


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

    # .env file doesn't exist. Init it.
    write_env_file(".env", [f"{browser_cmd_template}\n"])


def parse_app_init_file(file_path: str):
    """Returns imports and the rest as strings, used by the template"""
    with open(file_path, "r") as file:
        lines = file.readlines()

    import_lines = []
    main_code_lines = []

    # Iterate through the lines of the file
    for line in lines:
        if line.startswith("import"):
            import_lines.append(line)
        else:
            # we indent, since it will end up inside the add event listener callback, for format reasons
            main_code_lines.append(f"\t{line}")

    # Join the lines into multiline strings, note: lines already contain newline separator
    imports = "".join(import_lines)
    main_code = "".join(main_code_lines)

    return imports, main_code


def react_action(project_dir_path: str):
    react_init_file_path = get_react_init_file_path(project_dir_path)
    imports, main_code = parse_app_init_file(react_init_file_path)
    init_template_content = generate_init_template(imports=imports, main_code=main_code)

    # Write the modified content back to the file
    with open(react_init_file_path, "w") as file:
        file.write(init_template_content)

    patch_react_env_file()
