from __future__ import annotations

from enum import Enum
from typing import Callable
from typing import Final
from typing import Generic
from typing import Mapping
from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


class EnumDict(dict[K, V], Generic[K, V]):
    def __getitem__(self, item: K | Enum) -> V:
        if isinstance(item, Enum):
            return super().__getitem__(item.value)
        return super().__getitem__(item)


class enum_property(Generic[V]):
    def __init__(self, mapping: Mapping[object, V]) -> None:
        self.mapping: Final = EnumDict(mapping)
        self.bound_name: str | None = None

    def __set_name__(self, owner: type[Enum], name: str) -> None:
        self.bound_name = name

    def __get__(self, instance: Enum, owner: type[Enum]) -> V:
        assert self.bound_name is not None
        try:
            return self.mapping[instance]
        except KeyError as e:
            raise AttributeError(
                f"{instance} has no attribute {self.bound_name!r}"
            ) from e


E = TypeVar("E")


def enum_getter(mapping: Mapping[K, V]) -> Callable[[E], V]:
    getter = EnumDict(mapping).__getitem__

    def method(self: E) -> V:
        assert isinstance(self, Enum)
        return getter(self)

    return method
