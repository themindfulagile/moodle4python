"""
Minimal in-process event bus — mirrors Moodle's hook/event system.
Handlers are registered at startup and called synchronously for now.
Celery integration (MTP-92) will make this async.
"""
from collections import defaultdict
from collections.abc import Callable
from typing import Any

_handlers: dict[str, list[Callable]] = defaultdict(list)


def subscribe(event: str, handler: Callable) -> None:
    _handlers[event].append(handler)


def emit(event: str, payload: Any = None) -> None:
    for handler in _handlers.get(event, []):
        handler(payload)
