from __future__ import absolute_import
from .base import *

import dj_database_url

ENV = 'HEROKU'
DEBUG = False
ALLOWED_HOSTS = [
    'neurobrush.com'
]
# ALLOWED_HOSTS = ['*']

DATABASES = {	
    'default': dj_database_url.config()
}

INSTALLED_APPS += (
    'gunicorn',
)

# INSTALLED_APPS = INSTALLED_APPS + (
#     'raven.contrib.django.raven_compat',
# )

STATICFILES_ROOT = PROJECT_DIR.child('static')
STATIC_URL = '//' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
