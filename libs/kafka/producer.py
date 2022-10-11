from confluent_kafka import Producer

import socket

conf = {'bootstrap.servers': "host1:9092,host2:9092",
        'client.id': socket.gethostname()}


class KafkaProducer:
    def __init__(self):
        self.producer = Producer(conf)

    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))

        else:
            print("Message produced: %s" % (str(msg)))

    def produce(
            self,
            topic: str,
            key: str,
            value: str):
        self.producer.produce(topic, key=key, value=value, callback=KafkaProducer.acked)
