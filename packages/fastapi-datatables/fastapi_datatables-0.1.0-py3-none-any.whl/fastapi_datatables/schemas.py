from __future__ import annotations
from abc import abstractmethod

from pydantic import BaseModel
from typing import Callable, Iterator, get_type_hints, Union, Any, Optional


class FieldsView:
    def __init__(self, items: set[str]) -> None:
        self._items = items

    def __rmatmul__(self, other: Union[str, Any]) -> FieldsView:
        if isinstance(other, str):
            return FieldsView(
                {f"{other}.{item.split('.')[-1]}" for item in self._items}
            )
        return NotImplemented

    def __add__(self, other: Union[FieldsView, Any]) -> FieldsView:
        if isinstance(other, FieldsView):
            return FieldsView(self._items | other._items)
        return NotImplemented

    def __str__(self) -> str:
        return f"FieldsView({', '.join(sorted(self._items))})"

    def __iter__(self) -> Iterator[str]:
        return iter(self._items)

    __repr__ = __str__


IGNORE_FIELDS_ATTR_NAME = "__ignore_fields__"


class Filterable:
    @classmethod
    def fields(cls, table_name: Optional[str] = None) -> FieldsView:
        res = FieldsView(
            set(get_type_hints(cls))
            - (
                set()
                if not hasattr(cls, IGNORE_FIELDS_ATTR_NAME)
                else set(getattr(cls, IGNORE_FIELDS_ATTR_NAME))
            )
        )
        if table_name is None:
            return res
        return table_name @ res

    @classmethod
    def filter(cls) -> Callable:
        raise NotImplementedError
