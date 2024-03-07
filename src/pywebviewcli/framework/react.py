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
