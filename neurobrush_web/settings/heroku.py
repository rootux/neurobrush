from __future__ import absolute_import
from .base import *

import dj_database_url

ENV = 'HEROKU'
DEBUG = True
ALLOWED_HOSTS = [
    'neurobrush.com'
]
# ALLOWED_HOSTS = ['*']

# DATABASES = {	
#     'default': dj_database_url.config()
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INSTALLED_APPS += (
    'gunicorn',
)

# INSTALLED_APPS = INSTALLED_APPS + (
#     'raven.contrib.django.raven_compat',
# )

STATICFILES_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '//' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
