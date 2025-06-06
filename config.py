"""Project configuration powered by **Pydantic** settings.

This module exposes a single :class:`Settings` instance that reads values from
environment variables (optionally loaded from a ``.env`` file). Defaults are
provided so the application works out of the box.
"""

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    # Paths and files
    listings_csv: str = Field("listings.csv", env="LISTINGS_CSV")
    vector_db_dir: str = Field("chroma_db", env="VECTOR_DB_DIR")
    cache_file: str = Field("listings_cache.pkl", env="CACHE_FILE")
    images_dir: str = Field("images", env="IMAGES_DIR")
    default_image: str = Field("default_image.png", env="DEFAULT_IMAGE")

    # Search settings
    top_k: int = Field(5, env="TOP_K")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

