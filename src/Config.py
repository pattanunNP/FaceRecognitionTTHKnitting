from os import getenv
from dotenv import load_dotenv

config_dotenv_path = './.env'

RABBITMQ_BROKER = getenv("RABBITMQ_BROKER")

REDIS_HOST_URL = getenv("REDIS_HOST_URL")
