from calendar import c
from re import S
import time
from base64 import b64encode
from pathlib import Path

import cv2
import numpy as np
from loguru import logger
from infrastructure.kafka.consumer import KafkaConsumer


class Consumer:

    def __init__(self):
        self.messageQueue = KafkaConsumer(topic_name="face-recognition")
        self.messageQueue.subscribe()

    def run(self):
        logger.info("running")
        self.messageQueue.consume()


if __name__ == "__main__":
    rp = Consumer()
    rp.run()
