# what_to_watch/settings.py

import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Базовый класс конфигурации."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL',
        'sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
