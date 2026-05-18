from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.config.yaml_loader import YAMLLoader

# =========================================================
# YAML CONFIGURATION LOADING
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CONFIG_PATH = BASE_DIR / "config" / "application.yaml"

yaml_config = YAMLLoader.load_yaml(str(CONFIG_PATH))


# =========================================================
# APPLICATION SETTINGS MODELS
# =========================================================


class ApplicationSettings(BaseModel):
    name: str
    version: str
    environment: str


class LoggingSettings(BaseModel):
    level: str
    file: str


class GitSettings(BaseModel):
    auto_stage: bool
    conventional_commits: bool


class AISettings(BaseModel):
    provider: str
    model: str
    host: str


class WatcherSettings(BaseModel):
    debounce_seconds: int


# =========================================================
# MAIN SETTINGS
# =========================================================


class Settings(BaseSettings):
    """
    Central application settings.
    """

    application: ApplicationSettings
    logging: LoggingSettings
    git: GitSettings
    ai: AISettings
    watcher: WatcherSettings

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


# =========================================================
# SETTINGS INSTANCE
# =========================================================

settings = Settings(
    application=ApplicationSettings(**yaml_config.get("application", {})),
    logging=LoggingSettings(**yaml_config.get("logging", {})),
    git=GitSettings(**yaml_config.get("git", {})),
    ai=AISettings(**yaml_config.get("ai", {})),
    watcher=WatcherSettings(**yaml_config.get("watcher", {})),
)
