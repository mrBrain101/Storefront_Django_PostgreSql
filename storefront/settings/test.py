from .common import *
from .dev import *


if RUNNING_IN_CONTAINER:
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("DATABASE_ENGINE"),
            'NAME': os.environ.get("TEST_DATABASE_NAME"),
            'USER': os.environ.get("TEST_DATABASE_USERNAME"),
            'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
            'HOST': os.environ.get("DATABASE_HOST"),
            'PORT': os.environ.get("DATABASE_PORT"),
        }
    }
else:
 DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'storefront',
            'USER': 'user',
            'PASSWORD': 'pytest',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }