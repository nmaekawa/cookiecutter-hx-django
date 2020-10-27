import os

from .base import *  # noqa
from .base import BASE_DIR

DEBUG = True

# test db is sqlite3
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "{{cookiecutter.project_slug}}-test-sqlite3.db"),
    },
}
