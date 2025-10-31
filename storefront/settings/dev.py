import os
from sys import argv
from dotenv import load_dotenv
from .common import *

# Load environment variables from .env file
load_dotenv()
RUNNING_IN_CONTAINER = os.environ.get('RUNNING_IN_CONTAINER', 'False').strip().lower()
RUNNING_IN_CONTAINER = RUNNING_IN_CONTAINER == 'true'

# DEBUG flag for development ONLY
DEBUG = os.environ['DEBUG'].strip().lower() == 'true'
# Set to True to enable profiling with silk in development
PROFILING = os.environ['SILK_PROFILING'].strip().lower() == 'true'

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
except:
    raise Exception('DJANGO_SECRET_KEY is not set in .env!')

# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
if RUNNING_IN_CONTAINER:
    ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(",")
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get("DATABASE_ENGINE"),
            'NAME': os.environ.get("DATABASE_NAME"),
            'USER': os.environ.get("DATABASE_USERNAME"),
            'PASSWORD': os.environ.get("DATABASE_PASSWORD"),
            'HOST': os.environ.get("DATABASE_HOST"),
            'PORT': os.environ.get("DATABASE_PORT"),
    }
}
else:
    # Service file path for Windows and PostgreSQL 18: 
    # '%APPDATA%\postgresql\.pg_service.conf'
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'OPTIONS': {
                'service' : 'storefront_service',
                'passfile' : '../.pgpass'
            }
        }
    }

# Email backend with smtp4dev
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 2525
DEFAULT_FROM_EMAIL = 'from@storefront.com'
ADMINS = [('Admin', 'admin@storefront.com')]

# CORS - enabling cross-origin requests for 8000/8001 ports
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8001',
    'http://127.0.0.1:8001'
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
    INTERNAL_IPS = [
        # ...
        '127.0.0.1'
        # ...
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True
    }

# Profiling with silk
if not TESTING and DEBUG and PROFILING:
    INSTALLED_APPS = [
        *INSTALLED_APPS,
        'silk'
    ]
    MIDDLEWARE = [
        'silk.middleware.SilkyMiddleware',
        *MIDDLEWARE
    ]

# Logging and generaL.log formatting.
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