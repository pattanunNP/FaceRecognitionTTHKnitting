import unittest
from .config import MilvusConfig
from .milvus import Milvus


class TestMilvusInfrastructure(unittest.TestCase):

    def test_milvus_initialize(self):
        milvusInstance = Milvus(MilvusConfig())

        self.assertIsInstance(milvusInstance, Milvus)


if __name__ == '__main__':
    unittest.main()
