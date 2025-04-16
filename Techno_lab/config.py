from pydantic import BaseModel
from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



HOSTNAME = "127.0.0.1"
USERNAME = "root"
PASSWORD = "root"
DB_NAME = "laba"


class DatabaseConnection(BaseModel):
    DATABASE_URL: str = f"mysql+aiomysql://{USERNAME}:{PASSWORD}@{HOSTNAME}/{DB_NAME}"

class Settings(BaseSettings):
    db_conn: DatabaseConnection =  DatabaseConnection()

settings = Settings()