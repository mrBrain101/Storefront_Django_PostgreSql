# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
from .common import *


DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DATABASE_ENGINE", 'django.db.backends.postgresql'),
        'NAME': os.environ.get("DATABASE_NAME", 'storefront'),
        'USER': os.environ.get("DATABASE_USERNAME", 'postgres'),
        'PASSWORD': os.environ.get("DATABASE_PASSWORD", 'postgresql'),
        'HOST': os.environ.get("DATABASE_HOST", 'localhost'),
        'PORT': os.environ.get("DATABASE_PORT", '5432'),
    }
}