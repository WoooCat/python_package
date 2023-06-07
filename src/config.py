from enum import Enum


class Configuration:
    """APP Configuration"""

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/api_db"


class TestingConfig(Configuration):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:postgres@localhost:5432/test_university_db"


class Config(str, Enum):
    development = "development"
    testing = "testing"


config = {
    Config.development: DevelopmentConfig,
    Config.testing: TestingConfig,
}