import os
import dj_database_url
from .common import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': dj_database_url.config(),
}
