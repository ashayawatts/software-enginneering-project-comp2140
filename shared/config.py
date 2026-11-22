"""Application configuration (local SQLite by default; cloud PostgreSQL via DATABASE_URL)."""

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-karmanjahni-change-in-production")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///karmanjahni.db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.environ.get("UPLOAD_FOLDER", "uploads")


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
