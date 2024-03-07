from react import react_action


def angular_action(project_dir_path: str):
    pass


def vue_action(project_dir_path: str):
    pass


action_map = {"react": react_action, "angular": angular_action, "vue": vue_action}


def do_additional_platform_init(framework_name: str, project_dir_path: str):
    action_map[framework_name](project_dir_path)
