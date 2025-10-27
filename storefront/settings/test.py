from .common import *
from .dev import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "storefront",
        "USER": "user",
        "PASSWORD": "pytest",
        "HOST": "localhost",
        "PORT": "5432",
    }
}