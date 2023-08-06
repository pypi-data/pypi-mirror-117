__all__ = [
    'AsyncInterfaceWrapper',
    'AsyncMultithreadWrapper',
    'ensure_async',
]
import asyncio.events
import typing


def ensure_async(func: typing.Callable) -> typing.Callable[..., typing.Awaitable]:
    """Ensure given callable is async.

    Note, that it doesn't provide concurrency by itself!
    It just allow to treat sync and async callables in the same way.

    Args:
        func: Any callable: synchronous or asynchronous.
    Returns:
        Wrapper that return awaitable object at call.
    """
    ...


class AsyncInterfaceWrapper(typing.Generic):
    """Wrap arbitrary object to be able to await any of it's methods even if it's sync.

    Note, that it doesn't provide concurrency by itself!
    It just allow to treat sync and async callables in the same way.
    """

    def __init__(self, wrapped: typing.TypeVar('T', bound=None)): ...


class AsyncMultithreadWrapper(typing.Generic):
    """Wrap arbitrary object to run each of it's methods in a separate thread.

    Examples:
        Simple usage example.

        >>> class SyncClassExample:
        >>>     def sync_method(self, sec):
        >>>         time.sleep(sec)  # Definitely not async.
        >>>         return sec
        >>>
        >>> obj = AsyncMultithreadWrapper(SyncClassExample())
        >>> await asyncio.gather(*[obj.sync_method(1) for _ in range(10)])
        ...
    """

    def __init__(
        self,
        wrapped: typing.TypeVar('T', bound=None),
        pool_size: int = 10,
        loop: typing.Optional[asyncio.events.AbstractEventLoop] = None
    ): ...
