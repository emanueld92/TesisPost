from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',

        'NAME': 'autismo',

        'USER': 'admin',

        'PASSWORD': 'Admin123..',

        'HOST': 'localhost',

        'PORT': '3306',

    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
