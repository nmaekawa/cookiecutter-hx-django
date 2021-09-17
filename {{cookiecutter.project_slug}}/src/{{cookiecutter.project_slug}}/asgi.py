"""
ASGI config for {{cookiecutter.project_slug}} project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from dotenv import load_dotenv

# if dotenv file, load it
# check env var, then a default.env in project root
dotenv_path = None
if "{{cookiecutter.project_slug | upper}}_DOTENV_PATH" in os.environ:
    dotenv_path = os.environ["{{cookiecutter.project_slug | upper}}_DOTENV_PATH"]
else:
    # check for default dotenv in project root
    managepy_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    default_env = os.path.join(managepy_dir, "default.env")
if os.path.exists(default_env):
    dotenv_path = default_env
if dotenv_path:
    load_dotenv(dotenv_path)

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "{{cookiecutter.project_slug}}.settings.prod",
)

application = get_asgi_application()
