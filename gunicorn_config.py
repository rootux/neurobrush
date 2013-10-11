from os import environ

bind = '0.0.0.0:%s' % environ.get('PORT')

workers = 4

worker_class = 'gevent'
