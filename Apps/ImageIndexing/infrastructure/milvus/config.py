from pydantic import BaseSettings, Field


class MilvusConfig(BaseSettings):
    MILVUS_ALIAS: str = Field(..., env="MILVUS_ALIAS")
    MILVUS_HOST: str = Field(..., env="MILVUS_HOST")
    MILVUS_PORT: str = Field(..., env="MILVUS_PORT")

    class Config:
        env_file_encoding = 'utf-8'
        case_sensitive = True
