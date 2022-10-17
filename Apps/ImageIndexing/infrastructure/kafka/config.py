from pydantic import BaseSettings, Field


class KafkaConfig(BaseSettings):
    KAFKA_SERVER: str = Field(..., env="KAFKA_SERVER")
    KAFKA_PORT: str = Field(..., env="KAFKA_PORT")
    KAFKA_CONSUMER_GROUP: str = Field(..., env="KAFKA_CONSUMER_GROUP")

    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True
