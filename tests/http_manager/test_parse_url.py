from src.http_manager.parse_url import is_http_url, parse_hostname_and_port


def test_parse_hostname_and_port():
    hostname, port = parse_hostname_and_port("http://localhost:3000")
    assert hostname == "localhost"
    assert port == 3000

    hostname, port = parse_hostname_and_port("http://example.com")
    assert hostname == "example.com"
    assert port == 80

    hostname, port = parse_hostname_and_port("https://example.com")
    assert hostname == "example.com"
    assert port == 443

    hostname, port = parse_hostname_and_port("https://google.com:8005/dwwwwdwqddw")
    assert hostname == "google.com"
    assert port == 8005


def test_is_http_url():
    assert is_http_url("http://localhost:5000") is True
    assert is_http_url("httplocalhost:5000") is False
    assert is_http_url("https://example.com") is True
    assert is_http_url("localhost.com") is False
