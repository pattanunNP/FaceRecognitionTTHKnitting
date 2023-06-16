from domain.registry import Registry
from adapter.all_requested_indexing import AllRequestedIndexingInMongo
from infrastructure.mongo import MongoDBConfig, MongoDB
from infrastructure.kafka import KafkaConfig, KafkaConsumer


def inject(loop):
    mongo_db = MongoDB(MongoDBConfig(), loop=loop).getDB()
    Registry().all_requested_task = AllRequestedIndexingInMongo(mongo_db)


def get_kafka_consumer(consumer_group: str):
    consumer = KafkaConsumer(consumer_group, KafkaConfig())
    return consumer
