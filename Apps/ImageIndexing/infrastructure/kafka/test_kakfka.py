import unittest

from confluent_kafka import Consumer

from .config import KafkaConfig
from .consumer import KafkaConsumer


class TestKafkaInfrastructure(unittest.TestCase):
    def test_kafka_instance(self):
        kafkaInstance = KafkaConsumer("face-recognition", KafkaConfig())

        self.assertIsInstance(kafkaInstance.getConsumer(), Consumer)


if __name__ == '__main__':
    unittest.main()
