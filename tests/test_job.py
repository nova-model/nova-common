"""Test package."""

from nova.common.job import WorkState


def test_workstate() -> None:
    state = WorkState.NOT_STARTED
    assert state.value == "not_started"
