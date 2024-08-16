from typing import Any, Type, TypeVar

try:
    from typing import TypeGuard
except ImportError:
    from typing_extensions import TypeGuard  # pip install typing-extensions

T = TypeVar("T")


def definitely(_obj: Any, _type: Type[T]) -> TypeGuard[T]:
    """Definitely typed.

    Forces any type on an object.

    Example
    -------

    .. code-block:: python

        name = "Fernando Miguel"
        assert definitely(name, int)

        reveal_type(definitely)
        #           ^^^^^^^^^^
        # runtime: str
        # TYPE_CHECKING: int

    Args:
        _obj (Any): The object to be force-typed.
        _type (type[T]): Any type to write.
    """
    return True
