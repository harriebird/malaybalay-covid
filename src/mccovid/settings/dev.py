# Development settings
# settings/dev.py
from .base import *

print("Running Development Settings.")

DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

SECRET_KEY = env('DJANGO_SECRET_KEY', default='CHANGEME!!BUTFuckIt!')

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# Add django_extensions to setup jupyter notebooks to work with our project
INSTALLED_APPS += ['debug_toolbar', 'django_extensions']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]

# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Load debug_toolbar middleware last
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# REST Framework Docs
# ------------------------------------------------------------------------------
# See: http://drfdocs.com/settings/
REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': False
}

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
