from __future__ import absolute_import
from os import environ
from .base import *

ENV = 'LOCAL'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1', 'localhost', 'local.dev')


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

STATIC_S3 = 'STATIC_S3' in environ

if DEBUG and not STATIC_S3:
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

