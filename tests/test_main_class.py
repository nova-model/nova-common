"""Test package."""

from nova.common import MainClass


def test_version() -> None:
    app = MainClass()
    assert app.name("test") == "test"
