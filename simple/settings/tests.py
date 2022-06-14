# flake8: noqa

import dj_database_url
from .base import *


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    "default": dj_database_url.config(
        default=config("DATABASE_URL", default="postgres://postgres:postgres@localhost:5432/initial"),
        conn_max_age=600,
    )
}


PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]


class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None
