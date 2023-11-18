import logging
from http_manager.parse_url import parse_hostname_and_port
from libs.wait_for_tcp_port import wait_for_port

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pywebviewclistartup")


def wait_for_server_startup(url: str, timeout: int):
    logger.info(f"Waiting for {url} to load...")
    try:
        hostname, port = parse_hostname_and_port(url)
        wait_for_port(port=port, host=hostname, timeout=timeout)
    except:
        pass
    logger.info(f"Done waiting for {url}  to load...")
