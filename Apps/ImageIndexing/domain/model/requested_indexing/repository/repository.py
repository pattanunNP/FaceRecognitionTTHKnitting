from abc import abstractmethod
from typing import List

from domain.base.repository import RepositoryAbstract
from ..requested_indexing import RequestedIndexing


class AllRequestedIndexing(RepositoryAbstract[str, RequestedIndexing]):
    @abstractmethod
    async def next_identity(self) -> str:
        pass

    @abstractmethod
    async def get_task_from_task_id(self, task_id: str) -> str:
        pass

    @abstractmethod
    async def are_pending(self) -> List[RequestedIndexing]:
        pass

    @abstractmethod
    async def from_id(self, id_: str) -> RequestedIndexing:
        pass

    @abstractmethod
    async def save(self, entity: RequestedIndexing):
        pass

    @abstractmethod
    async def add(self, entity: RequestedIndexing):
        pass
