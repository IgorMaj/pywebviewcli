def is_react(package_json: dict) -> bool:
    try:
        return bool(package_json["dependencies"]["react"])
    except:
        return False


def is_angular(package_json: dict) -> bool:
    try:
        return bool(package_json["dependencies"]["@angular/core"])
    except:
        return False


def is_vue(package_json: dict) -> bool:
    try:
        return bool(package_json["dependencies"]["vue"])
    except:
        return False


detect_chain = {"react": is_react, "angular": is_angular, "vue": is_vue}


def get_framework_name(package_json: dict) -> str:
    for framework_name in detect_chain:
        if detect_chain[framework_name](package_json):
            return framework_name
    return ""


def is_typescript(package_json: dict) -> bool:
    try:
        return (
            "dependencies" in package_json
            and "typescript" in package_json["dependencies"]
        ) or (
            "devDependencies" in package_json
            and "typescript" in package_json["devDependencies"]
        )
    except:
        return False
