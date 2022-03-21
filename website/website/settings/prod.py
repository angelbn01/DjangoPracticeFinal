import os

import django_heroku

DEBUG = False
ALLOWED_HOSTS = ["https://gentle-woodland-64586.herokuapp.com/", "https://gentle-woodland-64586.herokuapp.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd7bocj9olvt1qb',
        'HOST': 'ec2-54-226-18-238.compute-1.amazonaws.com',
        'USER': 'dstedknvotyxzq',
        'PASSWORD': '57a67724da5629ce2ff1813805f7d6427276ffff610e28bffc572d14b87ea2e9',
        'PORT': 5432,
    }
}
django_heroku.settings(locals())
