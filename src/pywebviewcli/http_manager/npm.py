import urllib.request
import json


def get_latest_package_version(package: str) -> str:
    url = f"https://registry.npmjs.org/{package}/latest"
    result = json.load(urllib.request.urlopen(url))
    return result["version"] if "version" in result else ""


def get_latest_concurrently_version():
    return get_latest_package_version("concurrently")
