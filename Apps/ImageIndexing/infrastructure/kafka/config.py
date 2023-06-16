from pydantic import BaseSettings, Field


class KafkaConfig(BaseSettings):
    KAFKA_SERVER: str = Field(..., env="KAFKA_SERVER")
    KAFKA_PORT: str = Field(..., env="KAFKA_PORT")
    KAFKA_CONSUMER_GROUP: str = Field(..., env="KAFKA_CONSUMER_GROUP")
    KAFKA_BROKER_URL: str = Field(..., env="KAFKA_BROKER_URL")
    KAFKA_CONSUMER_SESSION_TIMEOUT: int = Field(..., env="KAFKA_CONSUMER_SESSION_TIMEOUT")
    KAFKA_QUEUED_MAX_MESSAGE_K: int = Field(..., env="KAFKA_QUEUED_MAX_MESSAGE_K")
    
    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True
