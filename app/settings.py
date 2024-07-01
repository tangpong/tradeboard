from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    db_creds: str = Field(env="DB_CREDS")

    @property
    def db_url(self) -> str:
        return f"{self.db_creds}://pguser:pgpassword@localhost:5432/tradeboard"

    db_echo: bool = True


settings = Settings()
