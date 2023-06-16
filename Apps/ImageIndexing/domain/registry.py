from typing import Optional

from base.singleton import Singleton


class Registry(metaclass=Singleton):
    def __init__(self):
        from domain.model.requested_indexing.repository import AllRequestedIndexing

        self.all_requested_indexing: Optional[AllRequestedIndexing] = None
