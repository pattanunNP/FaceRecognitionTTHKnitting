from confluent_kafka import Consumer
from loguru import logger

from .config import KafkaConfig


class KafkaConsumer:

    def __init__(self, topic_name: str, config: KafkaConfig):
        conf = {
            'bootstrap.servers': f"{config.KAFKA_SERVER}:{config.KAFKA_PORT}",
            'group.id': f"{config.KAFKA_CONSUMER_GROUP}",
            'auto.offset.reset': 'earliest'
        }
        self.consumer = Consumer(conf)

        self.topic_name = topic_name

        logger.info("connected to consumer instance")

    def getConsumer(self):
        return self.consumer

    def getTopic(self):
        return self.topic_name
