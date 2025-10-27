import os
from sys import argv
from .common import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# For local development with DEBUG off and .pgpass and service files
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# For profiling with silk
PROFILING = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pq_95d_p%cok%2%mw$**q*#u9ohr7f9dcohtu5c=ghukj+(qlc'

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
# Service file path for Windows and PostgreSQL: 
# '%APPDATA%\postgresql\.pg_service.conf'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'storefront',
        'OPTIONS': {
            'service' : 'storefront_service',
            'passfile' : '../.pgpass'
        }
    }
}

# EMAIL
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@storefront.com'
ADMINS = [
    ('Admin', 'admin@storefront.com')
    ]

# Debug toolbar
INTERNAL_IPS = [
    # ...
    '127.0.0.1'
    # ...
]

# CORS
CORS_ALLOWED_ORIGINS = [
    # 'http://localhost:8001',
    # 'http://127.0.0.1:8001'
]

# Debug toolbar
# Only enable the toolbar when we're in debug mode and we're
# not running tests. Django will change DEBUG to be False for
# tests, so we can't rely on DEBUG alone.
TESTING = 'test' in argv or 'PYTEST_VERSION' in os.environ

if not TESTING and DEBUG:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        'debug_toolbar'
    ]
    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
        *MIDDLEWARE
    ]

if not TESTING and DEBUG and PROFILING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        'silk'
    ]
    MIDDLEWARE = [
        'silk.middleware.SilkyMiddleware',
        *MIDDLEWARE
    ]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} ({levelname}) - {name} - {message}',
            'style': '{',
        },
    },
}