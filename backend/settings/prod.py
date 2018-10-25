""" Production Settings """

import os
from .dev import *

############
# DATABASE #
############
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


############
# SECURITY #
############

DEBUG = False
# Set to your Domain here
ALLOWED_HOSTS = []
