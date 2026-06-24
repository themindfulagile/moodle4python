"""
Central settings — loaded once at startup via pydantic-settings.
All values can be overridden by environment variables or a .env file.
"""
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # App
    app_name: str = "Moodle Python API"
    app_version: str = "0.1.0"
    debug: bool = False
    environment: str = "development"

    # Database (connects to existing Moodle DB)
    database_url: str = "mysql+aiomysql://moodle:moodle@localhost:3306/moodle"
    db_pool_size: int = 10
    db_max_overflow: int = 20
    moodle_table_prefix: str = "mdl_"

    # JWT
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_access_token_expire_minutes: int = 60
    jwt_refresh_token_expire_days: int = 30

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # Observability
    log_level: str = "INFO"
    otel_exporter_otlp_endpoint: str = ""


@lru_cache
def get_settings() -> Settings:
    return Settings()
