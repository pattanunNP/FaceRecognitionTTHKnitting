import logging
import socket

import confluent_kafka

from .utils import delivery_report


class KafkaProducer:
    conf = {
        'bootstrap.servers': "localhost:9092,localhost:9092",
        'client.id': socket.gethostname()
    }

    def __init__(self, topic_name: str):
        self.producer = confluent_kafka.Producer(KafkaProducer.conf)

        self.topic_name = topic_name

        print("created producer instance")

    def send(self, message):
        try:
            self.producer.produce(self.topic_name,
                                  message,
                                  partition=0,
                                  callback=delivery_report)
            self.producer.flush()
        except Exception as err:
            logging.exception(err)
            self.producer.flush()
