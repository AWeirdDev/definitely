from typing import Dict, TypeVar

A = TypeVar("A")
B = TypeVar("B")


def reversely(__obj: Dict[A, B]) -> Dict[B, A]:
    """Definitely reversed KV-mapping of a dictionary.

    Examples
    --------

    .. code-block:: python

        data = {"password": 1234, "users": 100_000}
        rdata = reversely(data)
        assert rdata == {1234: "password", 100_000: "users"}

        reveal_type(data)   # dict[str, int]
        reveal_type(rdata)  # dict[int, str]

    Args:
        __obj (dict[A, B]): The dictionary to be reversed.

    Returns:
        dict[B, A]: The reversed dictionary.
    """
    result: Dict[B, A] = {}
    for k, v in __obj.items():
        result.update({v: k})

    return result
