from pydantic import BaseSettings, Field


class MongoDBConfig(BaseSettings):

    MONGODB_URI: str = Field(..., env="MONGODB_URI")

    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True
