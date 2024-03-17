from file_manager.methods import file_exists, read_json_file
from framework.common import parse_app_init_file
from templates.generate import generate_init_template


def find_nested_key_value(dict_obj: dict, requiredKey: str) -> str | None:
    if requiredKey in dict_obj:
        return dict_obj[requiredKey]

    for key in dict_obj:
        if type(dict_obj[key]) is dict:
            ret_val = find_nested_key_value(dict_obj[key], requiredKey)
            if ret_val is not None:
                return ret_val

    return None


def get_angular_build_output_path(project_dir_path: str) -> str:
    angular_json_path = f"{project_dir_path}/angular.json"
    if not file_exists(angular_json_path):
        raise Exception("Error: No angular.json file found.")

    json_content = read_json_file(angular_json_path)
    ret_val = find_nested_key_value(json_content, "outputPath")
    if ret_val:
        return ret_val
    raise Exception("Error: No 'outputPath' found in angular.json.")


def get_angular_init_file_path(project_dir_path: str) -> str:
    full_path = f"{project_dir_path}/src/main.ts"
    if file_exists(full_path):
        return full_path

    raise Exception("Error: No angular init file found.")


def angular_action(project_dir_path: str):
    angular_init_path = get_angular_init_file_path(project_dir_path)
    imports, main_code = parse_app_init_file(angular_init_path)
    init_template_content = generate_init_template(imports=imports, main_code=main_code)

    # Write the modified content back to the file
    with open(angular_init_path, "w") as file:
        file.write(init_template_content)
