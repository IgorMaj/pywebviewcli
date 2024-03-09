from angular import angular_action
from vue import vue_action
from react import react_action


action_map = {"react": react_action, "angular": angular_action, "vue": vue_action}


def do_additional_platform_init(framework_name: str, project_dir_path: str):
    action_map[framework_name](project_dir_path)
