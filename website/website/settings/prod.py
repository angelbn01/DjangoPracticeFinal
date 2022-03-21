import os

import django_heroku

DEBUG = True

ALLOWED_HOSTS = ["https://limitless-atoll-80517.herokuapp.com/", "https://limitless-atoll-80517.herokuapp.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db7q12vmoqpi1v',
        'HOST': 'ec2-3-211-217-45.compute-1.amazonaws.com',
        'USER': 'xgqlhnjnaztyth',
        'PASSWORD': '9694297fa49b5a3a1ff259faf26c4475dfb050ed50f344a1900b5bc89abe15df',
        'PORT': 5432,
    }
}
django_heroku.settings(locals())