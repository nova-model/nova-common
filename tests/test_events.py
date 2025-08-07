"""Test package."""

from typing import Any

import pytest

from nova.common import events
from nova.common.events import Event
from nova.common.signals import Signal


async def update_state_async(_sender: Any, value: int) -> int:
    return value


def update_state_sync(_sender: Any, value: int) -> int:
    return value


@pytest.fixture
def test_event() -> Event:
    id = "Test"
    event = events.get_event(Signal.TOOL_COMMAND, id)
    return event


@pytest.mark.asyncio
async def test_async(test_event: Any) -> None:
    test_event.connect(update_state_async)
    res = await test_event.send_async(id, value=1)
    assert res[0] == 1


def test_sync_uses_async(test_event: Any) -> None:
    test_event.connect(update_state_async)
    with pytest.raises(RuntimeError):
        test_event.send_sync(id)


@pytest.mark.asyncio
async def test_async_uses_sync(test_event: Any) -> None:
    test_event.connect(update_state_sync)
    res = await test_event.send_async(id, value=3)
    assert res[0] == 3


def test_sync(test_event: Any) -> None:
    test_event.connect(update_state_sync)
    res = test_event.send_sync(id, value=2)
    assert res[0] == 2
