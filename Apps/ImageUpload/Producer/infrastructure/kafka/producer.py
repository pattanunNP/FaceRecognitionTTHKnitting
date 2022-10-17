import logging
import socket
import confluent_kafka
from loguru import logger


class KafkaProducer:
    conf = {
        'bootstrap.servers': "localhost:9092,localhost:9092",
        'client.id': socket.gethostname()
    }

    def __init__(self, topic_name: str):
        self.producer = confluent_kafka.Producer(KafkaProducer.conf)

        self.topic_name = topic_name

        logger.info("created producer instance")

    def send(self, message):
        try:
            self.producer.poll(0)
            self.producer.produce(self.topic_name,
                                  message,
                                  partition=1,
                                  callback=KafkaProducer.delivery_report)
            self.producer.flush()
        except Exception as err:
            logging.exception(err)
            self.producer.flush()

    @staticmethod
    def delivery_report(err, msg):
        if err:
            logger.error("Failed to deliver message: {0}".format(err.str()))
        else:
            logger.info(f"msg produced. \n"
                        f"Topic: {msg.topic()} \n" +
                        f"Partition: {msg.partition()} \n" +
                        f"Offset: {msg.offset()} \n" +
                        f"Timestamp: {msg.timestamp()} \n")
