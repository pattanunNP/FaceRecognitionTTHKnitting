import motor.motor_asyncio
from loguru import logger

from .config import MongoDBConfig


class MongoDB:

    def __init__(self, config: MongoDBConfig, loop=None):
        uri = config.MONGODB_URI
        logger.info(f"MONGODB_URI: {uri}")
        if loop:
            client = motor.motor_asyncio.AsyncIOMotorClient(uri, io_loop=loop)
            logger.success(f"Connected to mongodb loop = {loop}")
        else:
            client = motor.motor_asyncio.AsyncIOMotorClient(uri)
            logger.success("Connected to mongodb loop")

        self.db = client.ImageIndexingService

    def getDB(self):
        return self.db
