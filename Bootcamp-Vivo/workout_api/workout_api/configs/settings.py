from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asynccpg://workout:workout@localhost/workout')

settings = Settings()
