from copy import deepcopy
from typing import Generic, TypeVar


CLASS = TypeVar('CLASS')


class BaseBuilder(Generic[CLASS]):
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(BaseBuilder, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.__values: dict[str, CLASS] = {}

    def register(self, value: CLASS, key: None | str):
        if key is None:
            key = value.__class__.__name__
        self.__values[key] = value

    def build(self, key: str, *args) -> CLASS:
        if key not in self.__values:
            raise KeyError(f"No {CLASS} found for {key=}")
        return deepcopy(self.__values[key])

    @property
    def values(self):
        return tuple(self.__values.keys())
