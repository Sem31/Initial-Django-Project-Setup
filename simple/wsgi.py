"""
WSGI config for simple project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

env_name = config("SIMPLE_ENVIRONMENT", default="local")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"simple.settings.{env_name}")

application = get_wsgi_application()
