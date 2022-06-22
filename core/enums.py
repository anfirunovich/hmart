from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)
