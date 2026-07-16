import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    APP_ENV = os.getenv("APP_ENV")
    DEBUG = os.getenv("DEBUG")


settings = Settings()
