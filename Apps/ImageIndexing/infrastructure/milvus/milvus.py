from loguru import logger
from pymilvus import connections

from .config import MilvusConfig


class Milvus:

    def __init__(self, config: MilvusConfig):
        logger.info(f"{config.MILVUS_ALIAS}->{config.MILVUS_HOST}:{config.MILVUS_PORT}")
        self.config = config
        self.connections = connections.connect(
            alias=self.config.MILVUS_ALIAS,
            host=self.config.MILVUS_HOST,
            port=self.config.MILVUS_PORT
        )

    def disconnect(self):
        self.connections.disconnect(self.config.MILVUS_ALIAS)
        logger.success(f"Disconnected from :{self.config.MILVUS_ALIAS}")
