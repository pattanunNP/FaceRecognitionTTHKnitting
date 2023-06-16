from typing import TYPE_CHECKING, List, Tuple

from pydantic import BaseModel, Field

from domain.base.repository import transaction
from domain.model.requested_indexing.repository.exception import DuplicateKeyError
from domain.model.requested_indexing.requested_indexing import RequestedIndexing
from registry import Registry


class TaskItem(BaseModel):
    _id: str = Field(..., alias='taskId')


class TaskState(BaseModel):
    id_: str = Field(..., alias='id')
    payload: dict
    status: str = 'pending'

    @classmethod
    def from_order(cls, task: RequestedIndexing) -> 'TaskState':
        tasks = []
        return cls(id=task.id_, payload=task.requested_payload, status=task.status)


@transaction
async def get_pending_orders() -> List[TaskState]:
    all_requested_orders = Registry().all_requested_indexing
    pending_orders = await all_requested_orders.are_pending()
    return [TaskState.from_order(pending_order) for pending_order in pending_orders]


@transaction
async def receive_requested_order(task_id: str, requested_payload) -> str:
    all_requested_task = Registry().all_requested_indexing

    id_: str = await all_requested_task.get_task_from_task_id(task_id)

    requested_task = RequestedIndexing(taskId=task_id, requestedPayload=requested_payload)
    try:
        await all_requested_task.add(requested_task)
    except DuplicateKeyError:  # duplicate message, do nothing
        print('key duplicated; just ignore')

    return id_


if TYPE_CHECKING:
    async def get_pending_task() -> List[TaskState]: ...


    async def receive_requested_task(source_id: str, customer_id: str, items: List[Tuple[str, int]]) -> str: ...
