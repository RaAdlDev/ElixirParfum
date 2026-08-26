from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_url_test: str
    secret_key: str
    database_url: str
    database_password: str
    database_user: str
    database_name: str
    token_duration: int
    algorithm: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()





