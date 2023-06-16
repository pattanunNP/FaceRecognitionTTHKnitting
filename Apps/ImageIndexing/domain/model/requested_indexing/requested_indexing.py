from typing import TYPE_CHECKING, Dict

from pydantic import Field, PrivateAttr

from domain.base.aggregate import AggregateBase

_ERR_MSG_EDIT_AFTER_SUBMIT = 'Submitted Task cannot be edited'
_ERR_MSG_DOUBLE_SUBMIT = 'Submitted Task cannot be submitted again'
_ERR_MSG_PAYLOAD_EMPTY = 'Task Payload cannot empty'


class RequestedIndexing(AggregateBase):
    id_: str = Field(..., alias='id')
    task_id: str = Field(..., alias='taskId')
    requested_payload: Dict = Field(..., alias='requestedPayload')
    status: str = 'pending'
    _version: int = PrivateAttr(default=0)

    def is_pending(self) -> bool:
        return self.status == 'pending'

    if TYPE_CHECKING:
        def __init__(self, *, id_: str,
                     taskId: str,
                     requestedPayload: Dict,
                     status: str = 'pending'
                     ):
            super().__init__()

    @property
    def version(self):
        return self._version
