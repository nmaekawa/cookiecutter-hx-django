"""
ASGI config for playaway project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

# if dotenv file, load it
dotenv_path = None
if "{{cookiecutter.project_prefix}}_DOTENV_PATH" in os.environ:
    dotenv_path = os.environ["{{cookiecutter.project_prefix}}_DOTENV_PATH"]
elif os.path.exists(os.path.join("{{cookiecutter.project_slug}}", "settings", ".env")):
    dotenv_path = os.path.join("{{cookiecutter.project_slug}}", "settings", ".env")
if dotenv_path:
    load_dotenv(dotenv_path)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{cookiecutter.project_slug}}.settings.prod",
)

application = get_asgi_application()
