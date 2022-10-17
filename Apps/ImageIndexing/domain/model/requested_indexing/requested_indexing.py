from typing import TYPE_CHECKING, Dict

from pydantic import Field, PrivateAttr

from domain.base.aggregate import AggregateBase

_ERR_MSG_EDIT_AFTER_SUBMIT = 'Submitted Order cannot be edited'
_ERR_MSG_DOUBLE_SUBMIT = 'Submitted Order cannot be submitted again'
_ERR_MSG_ITEM_AMOUNT_NOT_INTEGER = 'Order Item amount must be an integer'
_ERR_MSG_ITEM_AMOUNT_LESS_THAN_ZERO = 'Order Item amount cannot be less than 0'


class RequestedOrder(AggregateBase):
    id_: str = Field(..., alias='id')
    source_id: str = Field(..., alias='sourceId')
    requested_payload: Dict = Field(..., alias='requestedPayload')
    status: str = 'pending'
    _version: int = PrivateAttr(default=0)

    def is_pending(self) -> bool:
        return self.status == 'pending'

    if TYPE_CHECKING:
        def __init__(self, *, id_: str, sourceId: str, requestedPayload: Dict, status: str = 'pending'):
            super().__init__()

