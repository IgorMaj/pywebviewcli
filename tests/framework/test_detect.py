from src.pywebviewcli.framework.detect import (
    get_framework_name,
    is_angular,
    is_react,
    is_typescript,
    is_vue,
)


def test_is_react():
    assert not is_react(None)
    assert not is_react({})
    assert is_react({"dependencies": {"react": "*"}})


def test_is_angular():
    assert not is_angular(None)
    assert not is_angular({})
    assert is_angular({"dependencies": {"@angular/core": "*"}})


def test_is_vue():
    assert not is_vue(None)
    assert not is_vue({})
    assert is_vue({"dependencies": {"vue": "*"}})


def test_get_framework_name():
    assert get_framework_name({"dependencies": {"react": "*"}}) == "react"
    assert get_framework_name({"dependencies": {"@angular/core": "*"}}) == "angular"
    assert get_framework_name({"dependencies": {"vue": "*"}}) == "vue"
    assert get_framework_name({"dependencies": {"app": "*"}}) == ""


def test_is_typescript():
    assert not is_typescript(None)
    assert not is_typescript({})
    assert is_typescript({"dependencies": {"typescript": "*"}})
    assert is_typescript({"devDependencies": {"typescript": "*"}})
