import os
from .settings import *
import django_heroku

DEBUG = True
ALLOWED_HOSTS = ["gentle-woodland-64586.herokuapp.com"]
CSRF_TRUSTED_ORIGINS = ["https://gentle-woodland-64586.herokuapp.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("NAME_DB"),
        'HOST': os.environ.get("HOST_DB"),
        'USER': os.environ.get("USER_DB"),
        'PASSWORD': os.environ.get("PASSWORD_DB"),
        'PORT': '5432',
    }
}
django_heroku.settings(locals())
