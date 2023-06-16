from abc import ABC
from typing import List

import bson.errors
from bson.objectid import ObjectId
from pymongo.database import Database

from domain.model.requested_indexing import RequestedIndexing
from domain.model.requested_indexing.repository.exception import (
    InvalidTaskIdException, TaskNotFoundException, DuplicateKeyError,
    EntityOutdated)
from domain.port import AllRequestedIndexing


class AllRequestedIndexingInMongo(AllRequestedIndexing, ABC):

    def __init__(self, mongo_db: Database, collection_name: str = 'task'):
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    async def next_identity(self) -> str:
        return 'IN-' + str(ObjectId())

    async def get_task_from_task_id(self, task_id: str) -> str:
        try:
            task_id_random = task_id.split('-', maxsplit=1)[1]
        except IndexError:
            raise InvalidTaskIdException('Invalid Task ID')
        id_ = f'IN-{task_id_random}'
        return id_

    async def are_pending(self) -> List[RequestedIndexing]:
        filter_ = {'state.status': 'pending'}
        projection = {'_id': False, 'events': False}

        raw_orders = self.mongo_db[self.collection_name].find(
            filter_, projection)
        pending_orders = [(RequestedIndexing.deserialize(raw_order['state']),
                           raw_order['version'])
                          async for raw_order in raw_orders]
        for pending_order, version in pending_orders:
            pending_order._version = version
        return [pending_order for pending_order, _ in pending_orders]

    async def from_id(self, id_: str) -> RequestedIndexing:

        mongo_id = self._entity_id_to_mongo_id(id_)

        filter_ = {'_id': ObjectId(mongo_id)}
        projection = {'_id': False, 'events': False}

        raw = await self.mongo_db[self.collection_name
                                  ].find_one(filter_, projection)
        if raw is None:
            raise TaskNotFoundException(f'Order id {id_} not found')
        task = RequestedIndexing.deserialize(raw['state'])
        task._version = raw['version']
        return task

    async def save(self, entity: RequestedIndexing):
        data = entity.serialize()
        id_ = self._entity_id_to_mongo_id(entity.id_)

        current_version = entity.version
        spec = {'_id': id_, 'version': current_version}
        pending_events = [
            dict(**event.serialize(), version=current_version + 1 + i)
            for i, event in enumerate(entity.get_pending_events())
        ]
        update = {
            '$set': {
                'state': data
            },
            '$push': {
                'events': {
                    '$each': pending_events
                }
            },
            '$inc': {
                'version': len(pending_events)
            },
        }

        try:
            await self.mongo_db[self.collection_name].update_one(spec,
                                                                 update,
                                                                 upsert=True)
        except DuplicateKeyError:
            raise EntityOutdated()

    async def add(self, entity: RequestedIndexing):
        data = entity.serialize()
        id_ = self._entity_id_to_mongo_id(entity.id_)

        current_version = entity.version
        pending_events = [
            dict(**event.serialize(), version=current_version + 1 + i)
            for i, event in enumerate(entity.get_pending_events())
        ]
        document = {
            '_id': id_,
            'state': data,
            'events': pending_events,
            'version': current_version + len(pending_events),
        }

        try:
            await self.mongo_db[self.collection_name].insert_one(document)
        except DuplicateKeyError as e:
            raise e

    @staticmethod
    def _entity_id_to_mongo_id(id_: str) -> ObjectId:
        try:
            return ObjectId(id_.split('-', maxsplit=1)[1])
        except (IndexError, bson.errors.InvalidId):
            raise InvalidTaskIdException('Invalid Order id')
