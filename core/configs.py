from typing import List

from pydantic import BaseSettings, AnyHttpUrl
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação.
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = ''
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()