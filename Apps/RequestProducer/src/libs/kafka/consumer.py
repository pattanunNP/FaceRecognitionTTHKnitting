from confluent_kafka import Consumer
import socket

conf = {'bootstrap.servers': "host1:9092,host2:9092",
        'group.id': "foo",
        'auto.offset.reset': 'smallest'}


class KafkaConsumer:
    def __init__(self):
        self.producer = Consumer(conf)
