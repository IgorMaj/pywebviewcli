import urllib.parse

HTTP_PORT = 80
HTTPS_PORT = 443


def parse_hostname_and_port(url: str):
    parsed_obj = urllib.parse.urlsplit(url)
    port = None

    if parsed_obj.port:
        port = parsed_obj.port
    elif parsed_obj.scheme == "http":
        port = HTTP_PORT
    elif parsed_obj.scheme == "https":
        port = HTTPS_PORT

    return parsed_obj.hostname, port
