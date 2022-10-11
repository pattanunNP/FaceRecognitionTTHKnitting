import logging
from .utils import delivery_report, serializeImg
from confluent_kafka import Producer
import socket



class KafkaProducer:

    conf = {
        'bootstrap.servers': "localhost:9092,localhost:9092",
        'client.id': socket.gethostname()
        }

    def __init__(self, topic_name:str):
        self.producer = Producer(KafkaProducer.conf)

        self.topic_name = topic_name

        print("created producer instance")     

    def serializeImg(self, img):
        return serializeImg(img)
    

    def send(self, message):
        self.producer.produce(self.topic_name, message, callback=delivery_report)
        self.producer.flush()   