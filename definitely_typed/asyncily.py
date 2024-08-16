import asyncio
from typing import (
    AsyncIterator,
    Awaitable,
    Callable,
    Iterator,
    ParamSpec,
    TypeVar,
)

T = TypeVar("T")
P = ParamSpec("P")


def asyncily(fn: Callable[P, T]) -> Callable[P, Awaitable[T]]:
    """Run a function asynchronously.

    Examples
    --------

    You can use this as a decorator, and use it outside:

    .. code-block:: python

        @asyncily
        async def duplicate(object: str):
            return object * 2

        await duplicate("Money")  # "MoneyMoney"

    ...or treat it as a "async function factory":

    .. code-block:: python

        def greet(name: str):
            return "Hello, " + name + "!"

        agreet = asyncily(greet)
        await agreet("Logan Paul")  # "Hello, Logan Paul!"

    Args:
        fn (Callable[P, T]): The function to be asyncified.

    Returns:
        Callable[P, Awaitable[T]]: Wrapper.
    """

    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        return await asyncio.to_thread(fn, *args, **kwargs)

    return wrapper


async def asyncily_iterate(it: Iterator[T]) -> AsyncIterator[T]:
    """Iterate through an iterator asynchronously.

    Examples
    --------

    .. code-block:: python

        def get_resources():
            yield from ["banana", "guava", "apple"]

        async for resource in asyncily_iterate(get_resources()):
            print(resource)

        # Output:
        # banana
        # guava
        # apple

    Args:
        it (Iterator[T]): The iterator to be asyncified.

    Returns:
        AsyncIterator[T]: The asyncified iterator.
    """

    class Done(Exception): ...

    while True:

        def getnext() -> T:
            try:
                return it.__next__()
            except StopIteration:
                raise Done("done.")

        try:
            yield await asyncio.to_thread(getnext)
        except Done:
            break
