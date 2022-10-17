from abc import abstractmethod
from functools import wraps
from typing import TypeVar, Generic

IdType = TypeVar('IdType')

EntityType = TypeVar('EntityType')


class EntityNotFround(Exception):
    pass


class EntityOutdated(Exception):
    pass


class RepositoryAbstract(Generic[IdType, EntityType]):
    @abstractmethod
    async def next_identity(self) -> IdType:
        pass

    @abstractmethod
    async def from_id(self, id_: IdType) -> EntityType:
        pass

    @abstractmethod
    async def save(self, entity: EntityType):
        pass


def transaction(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        while True:
            try:
                return await func(*args, **kwargs)
            except EntityOutdated:
                continue

    return wrapper
