import os

from .base import *  # noqa
from .base import BASE_DIR

DEBUG = True

# local db is sqlite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(
            BASE_DIR, "{{cookiecutter.project_slug}}-local-sqlite3.db"
        ),
    },
}
