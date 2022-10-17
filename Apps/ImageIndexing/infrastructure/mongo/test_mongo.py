import unittest

from .config import MongoDBConfig
from .mongo import MongoDB


class TestMongoDBInfrastructure(unittest.TestCase):

    def test_initial_mongo(self):
        mongoInstance = MongoDB(MongoDBConfig())
        self.assertIsInstance(mongoInstance, MongoDB)


if __name__ == '__main__':
    unittest.main()
