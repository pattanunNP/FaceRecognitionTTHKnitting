from confluent_kafka import Consumer
from loguru import logger

from .config import KafkaConfig


class KafkaConsumer:
    def __init__(self, topic_name: str, config: KafkaConfig):
        conf = {
            'bootstrap.servers': config.KAFKA_BROKER_URL,
            'group.id': 'testgroup',
            'security.protocol': 'SASL_PLAINTEXT',
            'sasl.username': 'admin',
            'sasl.password': 'admin-secret',
            'sasl.mechanism': 'PLAIN',
            'default.topic.config': {
                'auto.offset.reset': 'smallest'
            },
            'session.timeout.ms': config.KAFKA_CONSUMER_SESSION_TIMEOUT,
            'queued.max.messages.kbytes': config.KAFKA_QUEUED_MAX_MESSAGE_K
        }
        self.consumer = Consumer(conf)

        self.topic_name = topic_name

        logger.info("connected to consumer instance")

    def getConsumer(self):
        return self.consumer

    def getTopic(self):
        return self.topic_name
